import QtQuick 1.0

Rectangle {

    property int overal_padding: 10

    id: main_window
    width: 640
    height: 480
    color: "#dedad3"
    gradient: Gradient {
        GradientStop { position: 0.0; color: "#dedad3" }
        GradientStop { position: 1.0; color: "#bebab3" }
    }

    // Spacer
    Rectangle {
        id: spacer
        visible: false
        width: 10
    }


    // Package list
    Rectangle {
        id: left_panel
        width: 200
        height: main_window.height
        color: "transparent"
        anchors.left: spacer.right
        anchors.leftMargin: overal_padding
/*
        Column {
            anchors.topMargin: overal_padding
            anchors.fill: parent
            spacing: 10
            */

            String {text: "Lorem ipsum dolor sit amet lor fsd ggjj"; color: "black"; id: "abcdef"}
            String {text: "druhy"; color: "black"; anchors.top: abcdef.bottom}
       // }
    }

    // Line
    Rectangle {
        id: center_line
        width: 1
        height: main_window.height
        anchors.left: left_panel.right
        anchors.leftMargin: overal_padding
        color: "grey"
    }

    // Right panel
    Rectangle {
        id: right_panel
        anchors.left: left_panel.right
        width: main_window.width - left_panel.width - right_panel.anchors.leftMargin
        height: main_window.height
        anchors.leftMargin: overal_padding * 2
        color: "transparent"

        Column {
            anchors.topMargin: overal_padding
            anchors.fill: parent
            spacing: 20

            Panel {
                id: "panel_name"
                header_text: "fedora-gooey-karma-5.3.4.rpm"
                content: String {text: "Six lorem ipsum dolor sit amet consetue lorem ipsum dolor sit amet lorem fedora gooey karma"; color: "black"}
                height: 100
            }

            Panel {
                id: "panel_bugs"
                header_text: "Bugs"
                content: String {text: "Tu budu bugy"; color: "black"}
                height: 100
            }

        }

    }

}

