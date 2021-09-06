import hashlib
import time


class CreateSign:
    def __init__(self):
        self.key = "dcq"

    def create(self, t):
        md5 = hashlib.md5()
        md5.update(bytes(t.encode("utf-8")))
        return md5.hexdigest()


def verify(t, sign) -> bool:
    time_time = time.time()
    if (int(time_time) - int(t)) < 30:
        s = CreateSign()
        if sign == s.create(str(t)):
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    t = time.time()
    print(t)
    md5 = hashlib.md5()
    md5.update(bytes(str(1630925214).encode("utf-8")))
    time.sleep(2)
    print(verify(1630925214, md5.hexdigest()))
