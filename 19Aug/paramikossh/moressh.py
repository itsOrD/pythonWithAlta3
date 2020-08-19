#!/usr/bin/python3
''' itsOrD || learning about Python SSH '''

# used to remove warnings from packages
import warnings
import paramiko

# filter out any warnings with the work Paramiko
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    # runtime code that calls other fxns
    # describe the conn data
    creds = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"},\
            {"un": "fry", "ip": "10.10.2.4"}]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across the collection creds
    for cred in creds:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print(f'''Connection to... {cred.get("un")}@{cred.get("ip")}''')

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home dir
        sshsession.exec_command(f'''touch /home/{cred.get("un")}/goodnews.everyone''')

        ## list the contents of each home dir
        sessin, sessout, sesserr = sshsession.exec_command(f'''ls /home/{cred.get("un")}''')

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()

    print('Nice loop.')

main()
