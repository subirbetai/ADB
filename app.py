import time

from libs.ADB import ADB

adb = ADB()
adb.devices()


class Run:

    def repeat(self):
        adb.clearButton()
        adb.tapButton('938', '1375')
        adb.tapButton('813', '1844')

        adb.aeroplane(1)
        time.sleep(1)
        adb.aeroplane(0)
        time.sleep(6)

        adb.openLink("https://bit.ly/3t1ZDad")
        time.sleep(14)

        adb.openApp('com.liamw.root.androididchanger', 'com.liamw.root.androididchanger.MainActivity')
        adb.tapButton(1020, 126)
        adb.tapButton(519, 472)

        adb.openApp('com.google.android.gms', 'com.google.android.gms.ads.settings.AdsSettingsActivity')
        time.sleep(3)
        adb.tapButton(443, 318)
        adb.tapButton(872, 1148)
        time.sleep(2)

        adb.homeButton()

        adb.tapButton('927', '1377')
        time.sleep(2)
        adb.tapButton('815', '1872')
        time.sleep(40)

        adb.tapButton('836', '1858')
        time.sleep(5)

        adb.uninstallApp('com.next.innovation.takatak')


if __name__ == "__main__":

    while True:
        run = Run()
        run.repeat()
