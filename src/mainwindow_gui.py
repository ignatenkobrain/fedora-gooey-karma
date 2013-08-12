# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Mon Aug 12 23:56:07 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 772)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralWidgetSplitter = QtGui.QVBoxLayout(self.centralwidget)
        self.centralWidgetSplitter.setObjectName("centralWidgetSplitter")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pkgLists = QtGui.QWidget(self.centralwidget)
        self.pkgLists.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pkgLists.setObjectName("pkgLists")
        self.verticalLayout = QtGui.QVBoxLayout(self.pkgLists)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.pkgLists)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchEdit = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.searchEdit.setFont(font)
        self.searchEdit.setInputMask("")
        self.searchEdit.setText("")
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.karmaCheckBox = QtGui.QCheckBox(self.groupBox)
        self.karmaCheckBox.setChecked(False)
        self.karmaCheckBox.setObjectName("karmaCheckBox")
        self.verticalLayout_5.addWidget(self.karmaCheckBox)
        self.karmaFilterWidget = QtGui.QWidget(self.groupBox)
        self.karmaFilterWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.karmaFilterWidget.setObjectName("karmaFilterWidget")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.karmaFilterWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.karmaFilterUserCombo = QtGui.QComboBox(self.karmaFilterWidget)
        self.karmaFilterUserCombo.setObjectName("karmaFilterUserCombo")
        self.karmaFilterUserCombo.addItem("")
        self.karmaFilterUserCombo.addItem("")
        self.verticalLayout_8.addWidget(self.karmaFilterUserCombo)
        self.karmaUsernameEdit = QtGui.QLineEdit(self.karmaFilterWidget)
        self.karmaUsernameEdit.setDragEnabled(False)
        self.karmaUsernameEdit.setObjectName("karmaUsernameEdit")
        self.verticalLayout_8.addWidget(self.karmaUsernameEdit)
        self.verticalLayout_5.addWidget(self.karmaFilterWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.installedBtn = QtGui.QPushButton(self.groupBox)
        self.installedBtn.setCheckable(True)
        self.installedBtn.setChecked(True)
        self.installedBtn.setAutoDefault(False)
        self.installedBtn.setDefault(False)
        self.installedBtn.setFlat(False)
        self.installedBtn.setObjectName("installedBtn")
        self.horizontalLayout.addWidget(self.installedBtn)
        self.availableBtn = QtGui.QPushButton(self.groupBox)
        self.availableBtn.setCheckable(True)
        self.availableBtn.setChecked(False)
        self.availableBtn.setAutoDefault(False)
        self.availableBtn.setDefault(False)
        self.availableBtn.setFlat(False)
        self.availableBtn.setObjectName("availableBtn")
        self.horizontalLayout.addWidget(self.availableBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.pkgList = QtGui.QListWidget(self.pkgLists)
        self.pkgList.setFrameShadow(QtGui.QFrame.Sunken)
        self.pkgList.setTabKeyNavigation(False)
        self.pkgList.setObjectName("pkgList")
        self.verticalLayout.addWidget(self.pkgList)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtGui.QLabel(self.pkgLists)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.maxDays = QtGui.QSpinBox(self.pkgLists)
        self.maxDays.setSuffix("")
        self.maxDays.setPrefix("")
        self.maxDays.setMinimum(1)
        self.maxDays.setMaximum(99999)
        self.maxDays.setProperty("value", 7)
        self.maxDays.setObjectName("maxDays")
        self.horizontalLayout_3.addWidget(self.maxDays)
        self.label_5 = QtGui.QLabel(self.pkgLists)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.releaseComboBox = QtGui.QComboBox(self.pkgLists)
        self.releaseComboBox.setObjectName("releaseComboBox")
        self.horizontalLayout_5.addWidget(self.releaseComboBox)
        self.loadPackagesBtn = QtGui.QPushButton(self.pkgLists)
        self.loadPackagesBtn.setObjectName("loadPackagesBtn")
        self.horizontalLayout_5.addWidget(self.loadPackagesBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addWidget(self.pkgLists)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(9000, 9000))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tabWhatToTest = QtGui.QWidget()
        self.tabWhatToTest.setAutoFillBackground(False)
        self.tabWhatToTest.setStyleSheet("")
        self.tabWhatToTest.setObjectName("tabWhatToTest")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tabWhatToTest)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolBoxWhatToTest = QtGui.QToolBox(self.tabWhatToTest)
        self.toolBoxWhatToTest.setObjectName("toolBoxWhatToTest")
        self.toolBoxWelcome = QtGui.QWidget()
        self.toolBoxWelcome.setGeometry(QtCore.QRect(0, 0, 712, 454))
        self.toolBoxWelcome.setObjectName("toolBoxWelcome")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.toolBoxWelcome)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowser_2 = QtGui.QTextBrowser(self.toolBoxWelcome)
        self.textBrowser_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser_2.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_7.addWidget(self.textBrowser_2)
        self.toolBoxWhatToTest.addItem(self.toolBoxWelcome, "")
        self.toolBoxNegativeKarma = QtGui.QWidget()
        self.toolBoxNegativeKarma.setGeometry(QtCore.QRect(0, 0, 712, 454))
        self.toolBoxNegativeKarma.setObjectName("toolBoxNegativeKarma")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.toolBoxNegativeKarma)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtGui.QLabel(self.toolBoxNegativeKarma)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.tool_pkg_list_negative = QtGui.QTreeWidget(self.toolBoxNegativeKarma)
        self.tool_pkg_list_negative.setObjectName("tool_pkg_list_negative")
        self.verticalLayout_9.addWidget(self.tool_pkg_list_negative)
        self.toolBoxWhatToTest.addItem(self.toolBoxNegativeKarma, "")
        self.toolBoxRunning = QtGui.QWidget()
        self.toolBoxRunning.setGeometry(QtCore.QRect(0, 0, 712, 454))
        self.toolBoxRunning.setObjectName("toolBoxRunning")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.toolBoxRunning)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tool_pkg_list_running = QtGui.QTreeWidget(self.toolBoxRunning)
        self.tool_pkg_list_running.setObjectName("tool_pkg_list_running")
        self.verticalLayout_12.addWidget(self.tool_pkg_list_running)
        self.toolBoxWhatToTest.addItem(self.toolBoxRunning, "")
        self.toolBoxFavorite = QtGui.QWidget()
        self.toolBoxFavorite.setGeometry(QtCore.QRect(0, 0, 712, 454))
        self.toolBoxFavorite.setObjectName("toolBoxFavorite")
        self.toolBoxFavoriteLayout = QtGui.QVBoxLayout(self.toolBoxFavorite)
        self.toolBoxFavoriteLayout.setObjectName("toolBoxFavoriteLayout")
        self.tool_pkg_list_favorite = QtGui.QTreeWidget(self.toolBoxFavorite)
        self.tool_pkg_list_favorite.setObjectName("tool_pkg_list_favorite")
        self.toolBoxFavoriteLayout.addWidget(self.tool_pkg_list_favorite)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tool_add_remove_pkg = QtGui.QWidget(self.toolBoxFavorite)
        self.tool_add_remove_pkg.setMinimumSize(QtCore.QSize(0, 0))
        self.tool_add_remove_pkg.setObjectName("tool_add_remove_pkg")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tool_add_remove_pkg)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_tool_remove_pkg = QtGui.QPushButton(self.tool_add_remove_pkg)
        self.btn_tool_remove_pkg.setObjectName("btn_tool_remove_pkg")
        self.horizontalLayout_9.addWidget(self.btn_tool_remove_pkg)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.tool_pkg_name = QtGui.QLineEdit(self.tool_add_remove_pkg)
        self.tool_pkg_name.setObjectName("tool_pkg_name")
        self.horizontalLayout_9.addWidget(self.tool_pkg_name)
        self.btn_tool_add_pkg = QtGui.QPushButton(self.tool_add_remove_pkg)
        self.btn_tool_add_pkg.setObjectName("btn_tool_add_pkg")
        self.horizontalLayout_9.addWidget(self.btn_tool_add_pkg)
        self.horizontalLayout_7.addWidget(self.tool_add_remove_pkg)
        self.toolBoxFavoriteLayout.addLayout(self.horizontalLayout_7)
        self.toolBoxWhatToTest.addItem(self.toolBoxFavorite, "")
        self.toolBoxIgnored = QtGui.QWidget()
        self.toolBoxIgnored.setGeometry(QtCore.QRect(0, 0, 712, 454))
        self.toolBoxIgnored.setObjectName("toolBoxIgnored")
        self.toolBoxIgnoredLayout = QtGui.QVBoxLayout(self.toolBoxIgnored)
        self.toolBoxIgnoredLayout.setObjectName("toolBoxIgnoredLayout")
        self.tool_pkg_list_ignored = QtGui.QTreeWidget(self.toolBoxIgnored)
        self.tool_pkg_list_ignored.setObjectName("tool_pkg_list_ignored")
        self.toolBoxIgnoredLayout.addWidget(self.tool_pkg_list_ignored)
        self.toolBoxWhatToTest.addItem(self.toolBoxIgnored, "")
        self.horizontalLayout_6.addWidget(self.toolBoxWhatToTest)
        self.tabWidget.addTab(self.tabWhatToTest, "")
        self.TabInfo = QtGui.QWidget()
        self.TabInfo.setCursor(QtCore.Qt.ArrowCursor)
        self.TabInfo.setStyleSheet("")
        self.TabInfo.setObjectName("TabInfo")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.TabInfo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_side = QtGui.QTabWidget(self.TabInfo)
        self.tabWidget_side.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget_side.setObjectName("tabWidget_side")
        self.tabPkg_info = QtGui.QWidget()
        self.tabPkg_info.setObjectName("tabPkg_info")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabPkg_info)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_6 = QtGui.QSplitter(self.tabPkg_info)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter_7 = QtGui.QSplitter(self.splitter_6)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.layoutWidget_2 = QtGui.QWidget(self.splitter_7)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pkgNameLabel = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pkgNameLabel.setFont(font)
        self.pkgNameLabel.setCursor(QtCore.Qt.ArrowCursor)
        self.pkgNameLabel.setMouseTracking(False)
        self.pkgNameLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pkgNameLabel.setAcceptDrops(False)
        self.pkgNameLabel.setObjectName("pkgNameLabel")
        self.verticalLayout_11.addWidget(self.pkgNameLabel)
        self.textBrowser = QtGui.QTextBrowser(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_11.addWidget(self.textBrowser)
        self.splitter_8 = QtGui.QSplitter(self.splitter_7)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.treeWidget_bugs = QtGui.QTreeWidget(self.splitter_8)
        self.treeWidget_bugs.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.treeWidget_bugs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_bugs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_bugs.setRootIsDecorated(False)
        self.treeWidget_bugs.setWordWrap(False)
        self.treeWidget_bugs.setColumnCount(2)
        self.treeWidget_bugs.setObjectName("treeWidget_bugs")
        self.treeWidget_test_cases = QtGui.QTreeWidget(self.splitter_8)
        self.treeWidget_test_cases.setRootIsDecorated(False)
        self.treeWidget_test_cases.setObjectName("treeWidget_test_cases")
        self.treeWidget_related_packages = QtGui.QTreeWidget(self.splitter_8)
        self.treeWidget_related_packages.setObjectName("treeWidget_related_packages")
        self.verticalLayout_6.addWidget(self.splitter_6)
        self.tabWidget_side.addTab(self.tabPkg_info, "")
        self.tabPkg_karma = QtGui.QWidget()
        self.tabPkg_karma.setObjectName("tabPkg_karma")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tabPkg_karma)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.tabPkg_karma)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.usernameEdit = QtGui.QLineEdit(self.tabPkg_karma)
        self.usernameEdit.setObjectName("usernameEdit")
        self.horizontalLayout_8.addWidget(self.usernameEdit)
        self.passwordEdit = QtGui.QLineEdit(self.tabPkg_karma)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_8.addWidget(self.passwordEdit)
        self.karmaBox = QtGui.QComboBox(self.tabPkg_karma)
        self.karmaBox.setObjectName("karmaBox")
        self.karmaBox.addItem("")
        self.karmaBox.addItem("")
        self.karmaBox.addItem("")
        self.horizontalLayout_8.addWidget(self.karmaBox)
        self.sendBtn = QtGui.QPushButton(self.tabPkg_karma)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout_8.addWidget(self.sendBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label_2 = QtGui.QLabel(self.tabPkg_karma)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.splitter = QtGui.QSplitter(self.tabPkg_karma)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.commentEdit = QtGui.QPlainTextEdit(self.splitter)
        self.commentEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.commentEdit.setObjectName("commentEdit")
        self.treeWidget_feedback = QtGui.QTreeWidget(self.splitter)
        self.treeWidget_feedback.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_feedback.setRootIsDecorated(False)
        self.treeWidget_feedback.setUniformRowHeights(False)
        self.treeWidget_feedback.setObjectName("treeWidget_feedback")
        self.treeWidget_feedback.header().setCascadingSectionResizes(False)
        self.treeWidget_feedback.header().setMinimumSectionSize(30)
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_13.addLayout(self.verticalLayout_2)
        self.tabWidget_side.addTab(self.tabPkg_karma, "")
        self.tabPkg_settings = QtGui.QWidget()
        self.tabPkg_settings.setObjectName("tabPkg_settings")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tabPkg_settings)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtGui.QLabel(self.tabPkg_settings)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.settings_pkg_cat_normal = QtGui.QRadioButton(self.tabPkg_settings)
        self.settings_pkg_cat_normal.setChecked(True)
        self.settings_pkg_cat_normal.setObjectName("settings_pkg_cat_normal")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.settings_pkg_cat_normal)
        self.settings_pkg_cat_favorite = QtGui.QRadioButton(self.tabPkg_settings)
        self.settings_pkg_cat_favorite.setObjectName("settings_pkg_cat_favorite")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.settings_pkg_cat_favorite)
        self.settings_pkg_cat_ignored = QtGui.QRadioButton(self.tabPkg_settings)
        self.settings_pkg_cat_ignored.setObjectName("settings_pkg_cat_ignored")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.settings_pkg_cat_ignored)
        self.pkg_settings_open_bodhi_update = QtGui.QPushButton(self.tabPkg_settings)
        self.pkg_settings_open_bodhi_update.setObjectName("pkg_settings_open_bodhi_update")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pkg_settings_open_bodhi_update)
        self.pkg_settings_download_source_rpm = QtGui.QPushButton(self.tabPkg_settings)
        self.pkg_settings_download_source_rpm.setObjectName("pkg_settings_download_source_rpm")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pkg_settings_download_source_rpm)
        self.label_8 = QtGui.QLabel(self.tabPkg_settings)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_10.addLayout(self.formLayout)
        self.tabWidget_side.addTab(self.tabPkg_settings, "")
        self.verticalLayout_4.addWidget(self.tabWidget_side)
        self.tabWidget.addTab(self.TabInfo, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.centralWidgetSplitter.addLayout(self.horizontalLayout_4)
        self.statusList = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusList.sizePolicy().hasHeightForWidth())
        self.statusList.setSizePolicy(sizePolicy)
        self.statusList.setMaximumSize(QtCore.QSize(16777215, 80))
        self.statusList.setMouseTracking(True)
        self.statusList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.statusList.setObjectName("statusList")
        self.centralWidgetSplitter.addWidget(self.statusList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBoxWhatToTest.setCurrentIndex(2)
        self.tabWidget_side.setCurrentIndex(0)
        self.karmaBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.karmaCheckBox, QtCore.SIGNAL("toggled(bool)"), self.karmaFilterWidget.setShown)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.searchEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.karmaBox, self.sendBtn)
        MainWindow.setTabOrder(self.sendBtn, self.loadPackagesBtn)
        MainWindow.setTabOrder(self.loadPackagesBtn, self.availableBtn)
        MainWindow.setTabOrder(self.availableBtn, self.pkgList)
        MainWindow.setTabOrder(self.pkgList, self.releaseComboBox)
        MainWindow.setTabOrder(self.releaseComboBox, self.installedBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Fedora Gooey Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Search packages...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaCheckBox.setText(QtGui.QApplication.translate("MainWindow", "User filter", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaFilterUserCombo.setItemText(0, QtGui.QApplication.translate("MainWindow", "Karma not submitted by user", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaFilterUserCombo.setItemText(1, QtGui.QApplication.translate("MainWindow", "Karma submitted by user", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaUsernameEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "username for karma filter", None, QtGui.QApplication.UnicodeUTF8))
        self.installedBtn.setText(QtGui.QApplication.translate("MainWindow", "Installed", None, QtGui.QApplication.UnicodeUTF8))
        self.availableBtn.setText(QtGui.QApplication.translate("MainWindow", "Available", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgList.setSortingEnabled(True)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Updated for last", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "days", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPackagesBtn.setText(QtGui.QApplication.translate("MainWindow", "Reload packages", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to<span style=\" font-weight:600;\"> Fedora Gooey Karma</span> tool which helps you with testing new updates for your Fedora.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To load updates, press lower-left <span style=\" font-weight:600;\">Reload packages</span> button. If you are not sure what you should test, wait until all packages are loaded and see sections below this text.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxWhatToTest.setItemText(self.toolBoxWhatToTest.indexOf(self.toolBoxWelcome), QtGui.QApplication.translate("MainWindow", "Fedora Gooey Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "It would be nice to re-test updates which has got negative karma. See these packages below.", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_pkg_list_negative.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxWhatToTest.setItemText(self.toolBoxWhatToTest.indexOf(self.toolBoxNegativeKarma), QtGui.QApplication.translate("MainWindow", "Updates with negative karma", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_pkg_list_running.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxWhatToTest.setItemText(self.toolBoxWhatToTest.indexOf(self.toolBoxRunning), QtGui.QApplication.translate("MainWindow", "Currently running applications", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_pkg_list_favorite.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_tool_remove_pkg.setText(QtGui.QApplication.translate("MainWindow", "Remove selected package", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_tool_add_pkg.setText(QtGui.QApplication.translate("MainWindow", "Add package", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxWhatToTest.setItemText(self.toolBoxWhatToTest.indexOf(self.toolBoxFavorite), QtGui.QApplication.translate("MainWindow", "Favorite packages", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_pkg_list_ignored.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBoxWhatToTest.setItemText(self.toolBoxWhatToTest.indexOf(self.toolBoxIgnored), QtGui.QApplication.translate("MainWindow", "Ignored packages", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWhatToTest), QtGui.QApplication.translate("MainWindow", "What to test", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgNameLabel.setText(QtGui.QApplication.translate("MainWindow", "Package name", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_bugs.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Bug id", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_bugs.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_test_cases.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Test cases", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_related_packages.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Related packages", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_side.setTabText(self.tabWidget_side.indexOf(self.tabPkg_info), QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "FAS credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "username", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "-1", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.karmaBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "+1", None, QtGui.QApplication.UnicodeUTF8))
        self.sendBtn.setText(QtGui.QApplication.translate("MainWindow", "Send Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Your comment", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.setSortingEnabled(True)
        self.treeWidget_feedback.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "#", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Karma", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_feedback.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_side.setTabText(self.tabWidget_side.indexOf(self.tabPkg_karma), QtGui.QApplication.translate("MainWindow", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Package category", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_pkg_cat_normal.setText(QtGui.QApplication.translate("MainWindow", "Normal package", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_pkg_cat_favorite.setText(QtGui.QApplication.translate("MainWindow", "Favorite package", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_pkg_cat_ignored.setText(QtGui.QApplication.translate("MainWindow", "Ignore this package", None, QtGui.QApplication.UnicodeUTF8))
        self.pkg_settings_open_bodhi_update.setText(QtGui.QApplication.translate("MainWindow", "Open bodhi update in web browser", None, QtGui.QApplication.UnicodeUTF8))
        self.pkg_settings_download_source_rpm.setText(QtGui.QApplication.translate("MainWindow", "Download source RPM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_side.setTabText(self.tabWidget_side.indexOf(self.tabPkg_settings), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabInfo), QtGui.QApplication.translate("MainWindow", "Package info", None, QtGui.QApplication.UnicodeUTF8))
        self.statusList.setToolTip(QtGui.QApplication.translate("MainWindow", "Press and hold mouse button to expand", None, QtGui.QApplication.UnicodeUTF8))
        self.statusList.setSortingEnabled(False)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About Fedora Gooey Karma", None, QtGui.QApplication.UnicodeUTF8))

