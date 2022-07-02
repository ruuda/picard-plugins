# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\plugins\genre_mapper\options_genre_mapper.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
)


class Ui_GenreMapperOptionsPage(object):
    def setupUi(self, GenreMapperOptionsPage):
        GenreMapperOptionsPage.setObjectName("GenreMapperOptionsPage")
        GenreMapperOptionsPage.resize(398, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GenreMapperOptionsPage.sizePolicy().hasHeightForWidth())
        GenreMapperOptionsPage.setSizePolicy(sizePolicy)
        self.vboxlayout = QtWidgets.QVBoxLayout(GenreMapperOptionsPage)
        self.vboxlayout.setSpacing(16)
        self.vboxlayout.setObjectName("vboxlayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gm_description = QtWidgets.QGroupBox(GenreMapperOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gm_description.sizePolicy().hasHeightForWidth())
        self.gm_description.setSizePolicy(sizePolicy)
        self.gm_description.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gm_description.setFont(font)
        self.gm_description.setObjectName("gm_description")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gm_description)
        self.verticalLayout.setContentsMargins(9, 9, 9, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.format_description = QtWidgets.QLabel(self.gm_description)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.format_description.sizePolicy().hasHeightForWidth())
        self.format_description.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.format_description.setFont(font)
        self.format_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.format_description.setWordWrap(True)
        self.format_description.setObjectName("format_description")
        self.verticalLayout.addWidget(self.format_description)
        self.verticalLayout_4.addWidget(self.gm_description)
        self.gm_replacement_pairs = QtWidgets.QGroupBox(GenreMapperOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gm_replacement_pairs.sizePolicy().hasHeightForWidth())
        self.gm_replacement_pairs.setSizePolicy(sizePolicy)
        self.gm_replacement_pairs.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gm_replacement_pairs.setFont(font)
        self.gm_replacement_pairs.setObjectName("gm_replacement_pairs")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gm_replacement_pairs)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.genre_mapper_first_match_only = QtWidgets.QCheckBox(self.gm_replacement_pairs)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.genre_mapper_first_match_only.setFont(font)
        self.genre_mapper_first_match_only.setChecked(False)
        self.genre_mapper_first_match_only.setObjectName("genre_mapper_first_match_only")
        self.verticalLayout_3.addWidget(self.genre_mapper_first_match_only)
        self.genre_mapper_replacement_pairs = QtWidgets.QPlainTextEdit(self.gm_replacement_pairs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genre_mapper_replacement_pairs.sizePolicy().hasHeightForWidth())
        self.genre_mapper_replacement_pairs.setSizePolicy(sizePolicy)
        self.genre_mapper_replacement_pairs.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.genre_mapper_replacement_pairs.setFont(font)
        self.genre_mapper_replacement_pairs.setObjectName("genre_mapper_replacement_pairs")
        self.verticalLayout_3.addWidget(self.genre_mapper_replacement_pairs)
        self.verticalLayout_4.addWidget(self.gm_replacement_pairs)
        self.vboxlayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(GenreMapperOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(GenreMapperOptionsPage)

    def retranslateUi(self, GenreMapperOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.gm_description.setTitle(_translate("GenreMapperOptionsPage", "Genre Mapper"))
        self.format_description.setText(_translate("GenreMapperOptionsPage", "<html><head/><body><p>These are the original / replacement pairs used to map one genre entry to another. Each pair must be entered on a separate line in the form:</p><p><span style=\" font-weight:600;\">[genre match test string]=[replacement genre]</span></p><p>Supported wildcards in the test string part of the mapping include \'*\' and \'?\' to match any number of characters and a single character respectively.  Blank lines and lines beginning with an equals sign (=) will be ignored. Case-insensitive tests are used when matching. Replacements will be made in the order they are found in the list. An example for mapping all types of Rock genres (e.g. Country Rock, Hard Rock, Progressive Rock) to &quot;Rock&quot; would be done using the following line:</p><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-weight:600;\">*rock*=Rock</span></pre><p>For more information please see the <a href=\"https://github.com/rdswift/picard-plugins/blob/2.0_RDS_Plugins/plugins/genre_mapper/docs/README.md\"><span style=\" text-decoration: underline; color:#0000ff;\">User Guide</span></a> on GitHub.<br/></p></body></html>"))
        self.gm_replacement_pairs.setTitle(_translate("GenreMapperOptionsPage", "Replacement Pairs"))
        self.genre_mapper_first_match_only.setText(_translate("GenreMapperOptionsPage", "Apply only the first matching replacement"))
        self.genre_mapper_replacement_pairs.setPlaceholderText(_translate("GenreMapperOptionsPage", "Enter replacement pairs (one per line)"))
