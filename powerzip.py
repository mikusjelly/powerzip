import io
import zipfile

class PowerZip:

    def __init__(self, zipfile_path):
        with open(zipfile_path, mode='rb') as f:
            self.data = io.BytesIO(f.read())
            self.pzip = zipfile.ZipFile(self.data)

    def close(self):
        self.pzip.close()

    def getinfo(self, name):
        return self.pzip.getinfo(name)

    def infolist(self):
        return self.pzip.infolist()

    def namelist(self):
        return self.pzip.namelist()

    def open(self, name, mode='r', pwd=None):
        return self.pzip.open(name, mode='r', pwd=None)

    def extract(self, member, path=None, pwd=None):
        return self.pzip.extract(member, path=None, pwd=None)

    def extractall(self, path=None, members=None, pwd=None):
        return self.pzip.extractall(path=None, members=None, pwd=None)

    def printdir(self):
        return self.pzip.printdir()

    def setpassword(self, pwd):
        return self.pzip.setpassword(pwd)

    def read(self, name, pwd=None):
        return self.pzip.read(name, pwd=None)

    def add(self, arcname, filepath):
        with open(filepath, 'rb') as f:
            fdata = f.read()

        mzip = io.BytesIO()
        zout = zipfile.ZipFile (mzip, mode="w")
        for item in self.pzip.infolist():
            data = self.pzip.read(item.filename)
            if item.filename != arcname:
                zout.writestr(item, data)

        zout.writestr(arcname, fdata)
        zout.close()

        self.data = mzip
        self.pzip = zipfile.ZipFile(self.data)

    def delete(self, arcname):
        mzip = io.BytesIO()
        zout = zipfile.ZipFile (mzip, mode="w")
        for item in self.pzip.infolist():
            data = self.pzip.read(item.filename)
            if item.filename != arcname:
                zout.writestr(item, data)

        zout.close()

        self.data = mzip
        self.pzip = zipfile.ZipFile(self.data)

    def save(self, filename):
        pzip = zipfile.ZipFile(self.data)
        zout = zipfile.ZipFile (filename, 'w')
        for item in pzip.infolist():
            dat = pzip.read(item.filename)
            zout.writestr(item, dat)
        zout.close()
