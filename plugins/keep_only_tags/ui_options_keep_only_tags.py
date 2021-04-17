# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeepOnlyTagsOptionsPage(object):
    def setupUi(self, KeepOnlyTagsOptionsPage):
        KeepOnlyTagsOptionsPage.setObjectName("KeepOnlyTagsOptionsPage")
        KeepOnlyTagsOptionsPage.resize(561, 802)
        KeepOnlyTagsOptionsPage.setMinimumSize(QtCore.QSize(0, 0))
        KeepOnlyTagsOptionsPage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(KeepOnlyTagsOptionsPage)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(KeepOnlyTagsOptionsPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(KeepOnlyTagsOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.gb_list_of_tags = QtWidgets.QGroupBox(KeepOnlyTagsOptionsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_list_of_tags.sizePolicy().hasHeightForWidth())
        self.gb_list_of_tags.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.gb_list_of_tags.setFont(font)
        self.gb_list_of_tags.setObjectName("gb_list_of_tags")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gb_list_of_tags)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tag_list_text = QtWidgets.QTextEdit(self.gb_list_of_tags)
        self.tag_list_text.setObjectName("tag_list_text")
        self.verticalLayout_4.addWidget(self.tag_list_text)
        self.verticalLayout_6.addWidget(self.gb_list_of_tags)
        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.retranslateUi(KeepOnlyTagsOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(KeepOnlyTagsOptionsPage)

    def retranslateUi(self, KeepOnlyTagsOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        KeepOnlyTagsOptionsPage.setWindowTitle(_("Form"))
        self.label.setText(_("Keep Only Tags"))
        self.label_2.setText(_("<html><head/><body><p>These settings will determine which tags are written to the output files by Picard. Tags that you wish to keep are entered below, with each tag on a separate line. Blank lines will be ignored. The entries are not case-sensitive.</p><p>If a tag in the list ends with an asterisk (*), then it will keep any tags beginning with the tag.  For example, if your list contains &quot;<span style=\" font-weight:600;\">performer:*</span>&quot; then all tags beginning with &quot;<span style=\" font-weight:600;\">performer:</span>&quot; will be kept, such as &quot;<span style=\" font-weight:600;\">performer:instrument</span>&quot; and &quot;<span style=\" font-weight:600;\">performer:vocals</span>&quot;.</p><p>All tags that are removed will still be available as variables with &quot;<span style=\" font-weight:600;\">_ko_</span>&quot; prepended to the tag name. For example, if you choose not to keep the &quot;<span style=\" font-weight:600;\">musicbrainz_trackid</span>&quot; tag, it will still be available to scripts as &quot;<span style=\" font-weight:600;\">_ko_musicbrainz_trackid</span>&quot;.</p></body></html>"))
        self.gb_list_of_tags.setTitle(_("Tags to Keep"))
