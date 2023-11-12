from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem
from kivymd.uix.button import MDIconButton
from kivy.uix.modalview import ModalView


class MainWindow(MDBoxLayout):
    ...


class RightButton(IRightBody, MDIconButton):
    ...


class ReceiptsItem(TwoLineAvatarIconListItem):
    ...


class MyModalView(ModalView):
    def search(self, text):
        print("Искать:", text)


class KitchenApp(MDApp):

    def open_modal_view(self):
        modal_view = MyModalView()
        modal_view.open()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M2"
        return MainWindow()



if __name__ == "__main__":
    KitchenApp().run()
