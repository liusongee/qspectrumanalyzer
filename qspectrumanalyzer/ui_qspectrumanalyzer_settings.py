# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qspectrumanalyzer/qspectrumanalyzer_settings.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets

class Ui_QSpectrumAnalyzerSettings(object):
    def setupUi(self, QSpectrumAnalyzerSettings):
        QSpectrumAnalyzerSettings.setObjectName("QSpectrumAnalyzerSettings")
        QSpectrumAnalyzerSettings.resize(600, 310)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSpectrumAnalyzerSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.backendComboBox = QtWidgets.QComboBox(QSpectrumAnalyzerSettings)
        self.backendComboBox.setObjectName("backendComboBox")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.backendComboBox)
        self.label = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.executableEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerSettings)
        self.executableEdit.setObjectName("executableEdit")
        self.horizontalLayout.addWidget(self.executableEdit)
        self.executableButton = QtWidgets.QToolButton(QSpectrumAnalyzerSettings)
        self.executableButton.setObjectName("executableButton")
        self.horizontalLayout.addWidget(self.executableButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.deviceEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerSettings)
        self.deviceEdit.setObjectName("deviceEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deviceEdit)
        self.label_4 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.sampleRateSpinBox = QtWidgets.QSpinBox(QSpectrumAnalyzerSettings)
        self.sampleRateSpinBox.setMinimum(0)
        self.sampleRateSpinBox.setMaximum(25000000)
        self.sampleRateSpinBox.setSingleStep(10000)
        self.sampleRateSpinBox.setProperty("value", 2560000)
        self.sampleRateSpinBox.setObjectName("sampleRateSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sampleRateSpinBox)
        self.label_2 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.waterfallHistorySizeSpinBox = QtWidgets.QSpinBox(QSpectrumAnalyzerSettings)
        self.waterfallHistorySizeSpinBox.setMinimum(1)
        self.waterfallHistorySizeSpinBox.setMaximum(10000000)
        self.waterfallHistorySizeSpinBox.setProperty("value", 100)
        self.waterfallHistorySizeSpinBox.setObjectName("waterfallHistorySizeSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.waterfallHistorySizeSpinBox)
        self.label_6 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.paramsEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerSettings)
        self.paramsEdit.setObjectName("paramsEdit")
        self.horizontalLayout_3.addWidget(self.paramsEdit)
        self.helpButton = QtWidgets.QToolButton(QSpectrumAnalyzerSettings)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_3.addWidget(self.helpButton)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(QSpectrumAnalyzerSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.backendComboBox)
        self.label.setBuddy(self.executableEdit)
        self.label_5.setBuddy(self.deviceEdit)
        self.label_4.setBuddy(self.sampleRateSpinBox)
        self.label_2.setBuddy(self.waterfallHistorySizeSpinBox)
        self.label_6.setBuddy(self.paramsEdit)

        self.retranslateUi(QSpectrumAnalyzerSettings)
        self.buttonBox.accepted.connect(QSpectrumAnalyzerSettings.accept)
        self.buttonBox.rejected.connect(QSpectrumAnalyzerSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerSettings)
        QSpectrumAnalyzerSettings.setTabOrder(self.backendComboBox, self.executableEdit)
        QSpectrumAnalyzerSettings.setTabOrder(self.executableEdit, self.executableButton)
        QSpectrumAnalyzerSettings.setTabOrder(self.executableButton, self.deviceEdit)
        QSpectrumAnalyzerSettings.setTabOrder(self.deviceEdit, self.paramsEdit)
        QSpectrumAnalyzerSettings.setTabOrder(self.paramsEdit, self.helpButton)
        QSpectrumAnalyzerSettings.setTabOrder(self.helpButton, self.sampleRateSpinBox)
        QSpectrumAnalyzerSettings.setTabOrder(self.sampleRateSpinBox, self.waterfallHistorySizeSpinBox)
        QSpectrumAnalyzerSettings.setTabOrder(self.waterfallHistorySizeSpinBox, self.buttonBox)

    def retranslateUi(self, QSpectrumAnalyzerSettings):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerSettings.setWindowTitle(_translate("QSpectrumAnalyzerSettings", "Settings - QSpectrumAnalyzer"))
        self.label_3.setText(_translate("QSpectrumAnalyzerSettings", "&Backend:"))
        self.backendComboBox.setItemText(0, _translate("QSpectrumAnalyzerSettings", "soapy_power"))
        self.backendComboBox.setItemText(1, _translate("QSpectrumAnalyzerSettings", "rx_power"))
        self.backendComboBox.setItemText(2, _translate("QSpectrumAnalyzerSettings", "rtl_power_fftw"))
        self.backendComboBox.setItemText(3, _translate("QSpectrumAnalyzerSettings", "rtl_power"))
        self.backendComboBox.setItemText(4, _translate("QSpectrumAnalyzerSettings", "hackrf_sweep"))
        self.label.setText(_translate("QSpectrumAnalyzerSettings", "E&xecutable:"))
        self.executableEdit.setText(_translate("QSpectrumAnalyzerSettings", "soapy_power"))
        self.executableButton.setText(_translate("QSpectrumAnalyzerSettings", "..."))
        self.label_5.setText(_translate("QSpectrumAnalyzerSettings", "&Device:"))
        self.label_4.setText(_translate("QSpectrumAnalyzerSettings", "Sa&mple rate:"))
        self.label_2.setText(_translate("QSpectrumAnalyzerSettings", "&Waterfall history size:"))
        self.label_6.setText(_translate("QSpectrumAnalyzerSettings", "Additional &parameters:"))
        self.helpButton.setText(_translate("QSpectrumAnalyzerSettings", "?"))

