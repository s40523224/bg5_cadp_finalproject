<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="leo.20171122223841.1"><vh>@settings</vh>
<v t="leo.20171122223841.2"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="leo.20171122223841.3"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="leo.20171122224051.1"><vh>有關本專案</vh>
<v t="leo.20171122224436.1"><vh>機械系統設計</vh></v>
<v t="leo.20171123132217.1"><vh>電子系統</vh></v>
<v t="leo.20171123132229.1"><vh>資訊系統</vh></v>
</v>
<v t="leo.20171122224218.1"><vh>目錄規劃</vh></v>
<v t="leo.20171123133716.1" a="E"><vh>@path ./../</vh>
<v t="leo.20171123133524.1"><vh>@path report</vh>
<v t="leo.20171123133535.1"><vh>@path latex</vh>
<v t="leo.20171123133551.1"><vh>@edit readme.md</vh></v>
</v>
<v t="leo.20171123133733.1" a="E"><vh>@path words</vh>
<v t="leo.20171123133741.1"><vh>@edit readme.md</vh></v>
</v>
</v>
<v t="leo.20171123133840.1"><vh>@path mech_design</vh>
<v t="leo.20171123133848.1"><vh>@path cad_designs</vh>
<v t="leo.20171123133901.1"><vh>@edit readme.md</vh></v>
</v>
<v t="leo.20171123133929.1"><vh>@path v-rep_models</vh>
<v t="leo.20171123133945.1"><vh>@edit readme.md</vh></v>
</v>
</v>
<v t="leo.20171123134046.1"><vh>@path eric6_project</vh>
<v t="leo.20171123134103.1" a="E"><vh>@path marble_monitor</vh>
<v t="leo.20171123134117.1"><vh>@edit readme.md</vh></v>
</v>
</v>
<v t="leo.20171123134232.1" a="E"><vh>@path elec_design</vh>
<v t="leo.20171123134244.1"><vh>@edit readme.md</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="leo.20171122223841.1"></t>
<t tx="leo.20171122223841.2">QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;'CherryPy', 'pytz', 'mako', 'beautifulsoup4', 'pymysql', 'peewee'
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="leo.20171122223841.3">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="leo.20171122224051.1">這是一個用於 2017 Fall 電腦輔助設計實習專用的 demo 專案

主倉儲位於 Github, 用來展示如何透過協同開發鋼球循環運動系統模擬與實作

此倉儲存在 Github 的 gh-pages 分支, 因為希望能夠同時利用網際投影片與網際網誌展示相關資料

</t>
<t tx="leo.20171122224218.1">users 為各用戶存各自的 .leo 檔案專用

mech_design - 機械系統設計相關檔案

elec_design - 電子控制設計相關檔案

eric6_project - 資訊系統設計相關檔案

report - 分組期末報告相關檔案 - 又分為 word 與 latex 兩個子目錄, 可以用任何系統編寫

其他目錄將會配合 Fossil SCM 中的 reveal 簡報與 Pelican 網誌, 隨後將會加入

</t>
<t tx="leo.20171122224436.1">開放使用任何 CAD 系統執行繪圖, 但是必須包含

設計構想說明

機構模擬

零件繪圖

組立件繪圖

各零組件工程圖

v-rep 運動系統模擬

驅動系統與軌道系統實作</t>
<t tx="leo.20171123132217.1">Arduino 與 Micro-Server 在 Tinkercad 模擬

伺服器馬達驅動實作</t>
<t tx="leo.20171123132229.1">以 PyQt5 開發用來控制 v-rep 運動模擬與實體的視窗監控系統</t>
<t tx="leo.20171123133524.1"></t>
<t tx="leo.20171123133535.1"></t>
<t tx="leo.20171123133716.1"></t>
<t tx="leo.20171123133733.1"></t>
<t tx="leo.20171123133840.1"></t>
<t tx="leo.20171123133848.1"></t>
<t tx="leo.20171123133929.1"></t>
<t tx="leo.20171123134046.1"></t>
<t tx="leo.20171123134103.1"></t>
<t tx="leo.20171123134232.1"></t>
</tnodes>
</leo_file>
