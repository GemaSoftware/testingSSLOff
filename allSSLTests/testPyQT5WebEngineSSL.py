from PyQt5 import QtCore, QtWidgets, QtNetwork, QtWebEngineWidgets


def set_ssl_protocol():
    default_config = QtNetwork.QSslConfiguration.defaultConfiguration()
    default_config.setProtocol(QtNetwork.QSsl.TlsV1_2)
    default_config.setPeerVerifyMode(QtNetwork.QSslSocket.PeerVerifyMode.VerifyNone)

    QtNetwork.QSslConfiguration.setDefaultConfiguration(default_config)


class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def certificateError(self, certificateError):
        print(certificateError.errorDescription(), certificateError.url(), certificateError.isOverridable())
        error = certificateError.error()
        certificateError.ignoreCertificateError()

        return True


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.webView = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.webView)
        page = WebEnginePage(self)
        self.webView.setPage(page)
        page.load(QtCore.QUrl("https://127.0.0.1:5000/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    set_ssl_protocol()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())