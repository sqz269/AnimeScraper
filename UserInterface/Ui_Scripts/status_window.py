# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UserInterface\Source\status_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatusWindow(object):
    def setupUi(self, StatusWindow):
        StatusWindow.setObjectName("StatusWindow")
        StatusWindow.resize(495, 662)
        self.centralwidget = QtWidgets.QWidget(StatusWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.log_group = QtWidgets.QGroupBox(self.centralwidget)
        self.log_group.setObjectName("log_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.log_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.log_message_window = QtWidgets.QGroupBox(self.log_group)
        self.log_message_window.setObjectName("log_message_window")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.log_message_window)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.log_window = QtWidgets.QTextBrowser(self.log_message_window)
        self.log_window.setStyleSheet("")
        self.log_window.setLineWidth(1)
        self.log_window.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.log_window.setDocumentTitle("")
        self.log_window.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.log_window.setMarkdown("")
        self.log_window.setOverwriteMode(False)
        self.log_window.setTabStopWidth(80)
        self.log_window.setAcceptRichText(True)
        self.log_window.setCursorWidth(1)
        self.log_window.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.log_window.setObjectName("log_window")
        self.horizontalLayout_4.addWidget(self.log_window)
        self.verticalLayout_3.addWidget(self.log_message_window)
        self.log_event_overview = QtWidgets.QGroupBox(self.log_group)
        self.log_event_overview.setObjectName("log_event_overview")
        self.gridLayout = QtWidgets.QGridLayout(self.log_event_overview)
        self.gridLayout.setObjectName("gridLayout")
        self.status_warnings_l = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_warnings_l.setFont(font)
        self.status_warnings_l.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_warnings_l.setStyleSheet("color: orange")
        self.status_warnings_l.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_warnings_l.setObjectName("status_warnings_l")
        self.gridLayout.addWidget(self.status_warnings_l, 0, 2, 1, 1)
        self.status_errors_l = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_errors_l.setFont(font)
        self.status_errors_l.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_errors_l.setStyleSheet("color: red")
        self.status_errors_l.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_errors_l.setObjectName("status_errors_l")
        self.gridLayout.addWidget(self.status_errors_l, 0, 0, 1, 1)
        self.status_warnings = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_warnings.setFont(font)
        self.status_warnings.setStyleSheet("color: Orange")
        self.status_warnings.setObjectName("status_warnings")
        self.gridLayout.addWidget(self.status_warnings, 0, 3, 1, 1)
        self.status_infos_l = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_infos_l.setFont(font)
        self.status_infos_l.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_infos_l.setStyleSheet("color: blue")
        self.status_infos_l.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_infos_l.setObjectName("status_infos_l")
        self.gridLayout.addWidget(self.status_infos_l, 0, 4, 1, 1)
        self.status_errors = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_errors.setFont(font)
        self.status_errors.setStyleSheet("color: red")
        self.status_errors.setObjectName("status_errors")
        self.gridLayout.addWidget(self.status_errors, 0, 1, 1, 1)
        self.status_tip_debug_msg = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.status_tip_debug_msg.setFont(font)
        self.status_tip_debug_msg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_tip_debug_msg.setObjectName("status_tip_debug_msg")
        self.gridLayout.addWidget(self.status_tip_debug_msg, 2, 0, 1, 6)
        self.status_infos = QtWidgets.QLabel(self.log_event_overview)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_infos.setFont(font)
        self.status_infos.setStyleSheet("color: blue")
        self.status_infos.setObjectName("status_infos")
        self.gridLayout.addWidget(self.status_infos, 0, 5, 1, 1)
        self.verticalLayout_3.addWidget(self.log_event_overview)
        self.log_event_ops = QtWidgets.QGroupBox(self.log_group)
        self.log_event_ops.setTitle("")
        self.log_event_ops.setObjectName("log_event_ops")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.log_event_ops)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logs_export = QtWidgets.QPushButton(self.log_event_ops)
        self.logs_export.setObjectName("logs_export")
        self.horizontalLayout.addWidget(self.logs_export)
        self.logs_clear_window = QtWidgets.QPushButton(self.log_event_ops)
        self.logs_clear_window.setObjectName("logs_clear_window")
        self.horizontalLayout.addWidget(self.logs_clear_window)
        self.verticalLayout_3.addWidget(self.log_event_ops)
        self.verticalLayout.addWidget(self.log_group)
        self.status_overview = QtWidgets.QGroupBox(self.centralwidget)
        self.status_overview.setObjectName("status_overview")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.status_overview)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.status_overall_progress = QtWidgets.QProgressBar(self.status_overview)
        font = QtGui.QFont()
        font.setPointSize(2)
        self.status_overall_progress.setFont(font)
        self.status_overall_progress.setProperty("value", 0)
        self.status_overall_progress.setTextVisible(False)
        self.status_overall_progress.setInvertedAppearance(False)
        self.status_overall_progress.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.status_overall_progress.setObjectName("status_overall_progress")
        self.gridLayout_2.addWidget(self.status_overall_progress, 1, 0, 1, 1)
        self.status_overview_text = QtWidgets.QGroupBox(self.status_overview)
        self.status_overview_text.setTitle("")
        self.status_overview_text.setObjectName("status_overview_text")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.status_overview_text)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.status_pages_completed = QtWidgets.QLabel(self.status_overview_text)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_pages_completed.setFont(font)
        self.status_pages_completed.setAlignment(QtCore.Qt.AlignCenter)
        self.status_pages_completed.setObjectName("status_pages_completed")
        self.gridLayout_3.addWidget(self.status_pages_completed, 0, 1, 1, 1)
        self.status_pages_completed_l = QtWidgets.QLabel(self.status_overview_text)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_pages_completed_l.setFont(font)
        self.status_pages_completed_l.setAlignment(QtCore.Qt.AlignCenter)
        self.status_pages_completed_l.setObjectName("status_pages_completed_l")
        self.gridLayout_3.addWidget(self.status_pages_completed_l, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.status_overview_text, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.status_overview)
        StatusWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StatusWindow)
        self.statusbar.setObjectName("statusbar")
        StatusWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatusWindow)
        QtCore.QMetaObject.connectSlotsByName(StatusWindow)

    def retranslateUi(self, StatusWindow):
        _translate = QtCore.QCoreApplication.translate
        StatusWindow.setWindowTitle(_translate("StatusWindow", "Scraper Status"))
        self.log_group.setTitle(_translate("StatusWindow", "Logger"))
        self.log_message_window.setTitle(_translate("StatusWindow", "Log Messages"))
        self.log_window.setHtml(_translate("StatusWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.log_event_overview.setTitle(_translate("StatusWindow", "Event Overview"))
        self.status_warnings_l.setText(_translate("StatusWindow", "Warnings:"))
        self.status_errors_l.setText(_translate("StatusWindow", "Errors:"))
        self.status_warnings.setText(_translate("StatusWindow", "0"))
        self.status_infos_l.setText(_translate("StatusWindow", "Infos:"))
        self.status_errors.setText(_translate("StatusWindow", "0"))
        self.status_tip_debug_msg.setText(_translate("StatusWindow", "*To access debug messages, please use the CLI."))
        self.status_infos.setText(_translate("StatusWindow", "0"))
        self.logs_export.setText(_translate("StatusWindow", "Export Logs"))
        self.logs_clear_window.setText(_translate("StatusWindow", "Clear Logs"))
        self.status_overview.setTitle(_translate("StatusWindow", "Status Overview"))
        self.status_pages_completed.setText(_translate("StatusWindow", "0"))
        self.status_pages_completed_l.setText(_translate("StatusWindow", "Pages Completed:"))
