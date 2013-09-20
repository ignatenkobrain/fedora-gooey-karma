import QtQuick 1.0

Item {
    id: panel_container
    width: parent.width - 30

    property alias header_text: header_text.text
    property alias content: loader.sourceComponent

    Rectangle {


        id: header_border
        width: parent.width
        gradient: Gradient {
            GradientStop { position: 0.0; color: "#111" }
            GradientStop { position: 0.5; color: "#222222" }
            GradientStop { position: 1.0; color: "#111" }
        }
        height: header_text.height + 15
        radius: 10

        Text {
            id: header_text
            //anchors.fill: parent
            anchors.left: parent.left
            y: 8
            anchors.leftMargin: 10
            color: "white"
            font.pixelSize: 12
            //font.bold: true
        }


        Loader {
            id: loader
            anchors.top: header_text.bottom
            width: header_border.width
            x: 10
            anchors.topMargin: 10
        }
    }
}
