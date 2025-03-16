from sqladmin import ModelView
from src.mesvere.models import Mesvere, MesvereQeydleri

class MesvereAdmin(ModelView, model=Mesvere):
    column_list = [Mesvere.id, Mesvere.basliq, Mesvere.mesvere_qeydleri, Mesvere.tarix]
    column_labels = {
        Mesvere.id: 'ID',
        Mesvere.basliq: 'Başlıq',
        Mesvere.mesvere_qeydleri: 'Məşvərə Qeydləri',
        Mesvere.tarix: 'Tarix'
    }
    page_size = 10

class MesvereQeydleriAdmin(ModelView, model=MesvereQeydleri):
    column_list = [MesvereQeydleri.id, MesvereQeydleri.basliq, MesvereQeydleri.aciqlama, MesvereQeydleri.bitibmi]
    column_labels = {
        MesvereQeydleri.id: 'ID',
        MesvereQeydleri.basliq: 'Başlıq',
        MesvereQeydleri.aciqlama: 'Açıqlama',
        MesvereQeydleri.bitibmi: 'Bitibmi',
    }
    page_size = 10