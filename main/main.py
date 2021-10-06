import glob

from SetupClient.setupClient import SetupClient

if __name__ == '__main__':
    requset_files = glob.glob('../request/*.*')
    for requset_file in requset_files:
        setup_client = SetupClient(requset_file)
