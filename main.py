from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from datetime import datetime

# Дизайн интерфейса на языке KV
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: self.theme_cls.bg_dark

    MDTopAppBar:
        title: "📢 SemkaApp"
        elevation: 4
        right_action_items: [["information", lambda x: app.show_info()]]
        md_bg_color: 0.1, 0.1, 0.1, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"

        MDTextField:
            id: search_field
            hint_text: "Найти в тексте..."
            mode: "rectangle"
            on_text: app.search_text(self.text)

        MDCard:
            orientation: "vertical"
            padding: "8dp"
            md_bg_color: 0.15, 0.15, 0.15, 1
            line_color: 0.5, 0, 1, 1 # Фиолетовая рамка как в оригинале

            MDScrollView:
                MDLabel:
                    id: news_label
                    text: "Ожидание загрузки..."
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Caption"
                    font_name: "Roboto" # На Android лучше использовать стандартный

    MDBoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: "60dp"
        padding: "10dp"
        spacing: "10dp"

        MDRaisedButton:
            id: update_btn
            text: "🔄 ОБНОВИТЬ"
            md_bg_color: 0.15, 0.65, 0.27, 1 # Зеленый
            on_release: app.load_news()

        MDLabel:
            id: status_label
            text: "✨ Готов"
            theme_text_color: "Hint"
            halign: "center"

        MDRaisedButton:
            text: "✕ ВЫХОД"
            md_bg_color: 0.86, 0.2, 0.27, 1 # Красный
            on_release: app.stop()
'''

class SemkaApp(MDApp):
    PASTEBIN_URL = "https://pastebin.com/raw/2V7sWegJ"
    full_content = ""

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        self.load_news()

    def load_news(self):
        self.root.ids.status_label.text = "⏳ Загрузка..."
        self.root.ids.update_btn.disabled = True
        # Используем UrlRequest для асинхронной загрузки (аналог threading)
        UrlRequest(self.PASTEBIN_URL, on_success=self.update_ui, on_error=self.on_error, timeout=5)

    def update_ui(self, request, result):
        self.full_content = result
        self.root.ids.news_label.text = result
        now = datetime.now().strftime("%H:%M")
        self.root.ids.status_label.text = f"✅ Обновлено в {now}"
        self.root.ids.update_btn.disabled = False

    def on_error(self, request, error):
        self.root.ids.status_label.text = "❌ Ошибка сети"
        self.root.ids.update_btn.disabled = False

    def search_text(self, query):
        if not query:
            self.root.ids.news_label.text = self.full_content
            return
        
        # На мобилках сложнее сделать подсветку цветом, 
        # поэтому мы просто фильтруем строки с поисковым запросом
        lines = self.full_content.split('\\n')
        filtered = [line for line in lines if query.lower() in line.lower()]
        self.root.ids.news_label.text = "\\n".join(filtered) if filtered else "Ничего не найдено"

    def show_info(self):
        # На Android лучше не использовать messagebox, а менять текст статуса или заголовок
        self.root.ids.news_label.text = "SemkaApp v0.1\\nАвтор: @plsemen\\nМониторинг новостей."

if __name__ == "__main__":
    SemkaApp().run()