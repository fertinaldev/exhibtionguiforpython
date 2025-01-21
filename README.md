```markdown
# Exhibition Theme

Exhibition Theme, PyQt5 kullanarak oluşturulmuş özelleştirilebilir bir GUI temasıdır. Bu tema, oyun hilesi veya mod menüsü gibi uygulamalar için tasarlanmıştır.

## Özellikler

- Özelleştirilebilir sekmeler ve gruplar
- Renkli üst çubuk
- Özel kaydırıcılar
- Çeşitli kontrol öğeleri (onay kutuları, açılır menüler, vb.)
- Klavye kısayolları ile gizleme/gösterme ve kapatma

## Kurulum

1. Bu depoyu klonlayın:
   ```
   git clone https://github.com/fertinaldev/exhibtionguiforpython.git
   ```
2. Gerekli bağımlılıkları yükleyin:
   ```
   pip install PyQt5
   ```


## Kullanım

Temel kullanım örneği:

```python
from exhibition_theme import create_exhibition_theme

def setup_tabs(window):
    # Combat tab
    tab1 = window.add_tab("", "path/to/combat_icon.png")
    tab1.addWidget(window.create_group_box("Criticals", ["Enable", "Hurttime"], {"Mode": ["Packet"]}), 0, 0)
    tab1.addWidget(window.create_group_box("AutoClicker", ["Enable", "Random"], {"Delay": [100, 50, 500]}), 0, 1)

    # Movement tab
    tab2 = window.add_tab("", "path/to/movement_icon.png")
    tab2.addWidget(window.create_group_box("Speed", ["Enable"], {"Mode": ["Ground", "Jump"]}), 0, 0)
    tab2.addWidget(window.create_group_box("Flight", ["Enable"], {"Mode": ["Vanilla", "Glide"]}), 0, 1)

    # Add more tabs and widgets as needed

if __name__ == '__main__':
    window, app = create_exhibition_theme()
    setup_tabs(window)
    window.show()
    app.exec_()
```

## Özelleştirme

Temayı özelleştirmek için `setup_tabs` fonksiyonunu değiştirebilirsiniz. Yeni sekmeler ekleyebilir, mevcut sekmeleri değiştirebilir veya kendi grup kutularınızı oluşturabilirsiniz.

### Sekme Ekleme

```python
tab = window.add_tab("", "path/to/icon.png")
```

### Grup Kutusu Ekleme

```python
tab.addWidget(window.create_group_box("GroupName", ["Checkbox1", "Checkbox2"], {"Slider1": [default, min, max]}), row, column)
```

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
```
