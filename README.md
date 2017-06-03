# media-upload

## NEW Version
### Run commands

```sh
git clone -b ansible https://github.com/pkozak2/media-upload
```

then:

```sh
cd media-upload
```
edit hosts.ini file and start:

```sh
ansible-playbook -i hosts.ini media-upload.yml
```

## OLD HELP
### Need to install:

sudo yum install pyhton-pip

sudo pip install boto3

sudo pip install pytest Flask

export PYTHONPATH=/home/ec2-user/media-upload


sudo apt-get install ffmpeg

