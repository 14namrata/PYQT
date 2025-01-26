import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Hello QML"

    Rectangle {
        width: 640
        height: 480
        color: "lightblue"

        Text {
            text: "Welcome to QML!"
            anchors.centerIn: parent
            font.pixelSize: 24
        }

        Button {
            text: "Click Me"
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: {
                console.log("Button clicked!")
            }
        }
    }
}
