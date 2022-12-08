import sys


from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication


from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView, WebEngineCertificateError


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super(QWebEnginePage, self).__init__()
    def certificateError(self, certificateError):
        print(certificateError.errorDescription(), certificateError.url(), certificateError.isOverridable())
        error = certificateError.error()
        if error == WebEngineCertificateError.SslPinnedKeyNotInCertificateChain:
            print("SslPinnedKeyNotInCertificateChain")
        elif error == WebEngineCertificateError.CertificateCommonNameInvalid:
            print("CertificateCommonNameInvalid")
        elif error == WebEngineCertificateError.CertificateDateInvalid:
            print("CertificateDateInvalid")
        elif error == WebEngineCertificateError.CertificateAuthorityInvalid:
            print("CertificateAuthorityInvalid")
        elif error == WebEngineCertificateError.CertificateContainsErrors:
            print("CertificateContainsErrors")
        if error == WebEngineCertificateError.CertificateNoRevocationMechanism:
            print("CertificateNoRevocationMechanism")
        elif error == WebEngineCertificateError.CertificateUnableToCheckRevocation:
            print("CertificateUnableToCheckRevocation")
        elif error == WebEngineCertificateError.CertificateRevoked:
            print("CertificateRevoked")
        elif error == WebEngineCertificateError.CertificateInvalid:
            print("CertificateAuthorityInvalid")
        elif error == WebEngineCertificateError.CertificateWeakSignatureAlgorithm:
            print("CertificateWeakSignatureAlgorithm")
        elif error == WebEngineCertificateError.CertificateNonUniqueName:
            print("CertificateNonUniqueName")
        elif error == WebEngineCertificateError.CertificateWeakKey:
            print("CertificateWeakKey")
        elif error == WebEngineCertificateError.CertificateNameConstraintViolation:
            print("CertificateNameConstraintViolation")
        elif error == WebEngineCertificateError.CertificateValidityTooLong:
            print("CertificateValidityTooLong")
        elif error == WebEngineCertificateError.CertificateTransparencyRequired:
            print("CertificateTransparencyRequired")

        return super(WebEnginePage, self).certificateError(certificateError)


def main(args):
    app = QApplication(args)
    webview = QWebEngineView()
    page = WebEnginePage()
    webview.setPage(page)
    page.load((QUrl("https://127.0.0.1:5000/")))
    webview.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
