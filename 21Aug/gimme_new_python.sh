sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

sudo apt install -y python3.8-venv build-essential python3.8-dev
source venv/bin/activate
python3 -m pip install wheel
