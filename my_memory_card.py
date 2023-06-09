#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    


app = QApplication([])


btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 


RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=14) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------
answers = [rbtn_1 ,rbtn_2, rbtn_3, rbtn_4]

question_list = []





def show_correct(otvet):
    lb_Result.setText(otvet)
    show_result()

def  check_answer():
    
    if answers[0].isChecked():
        window.true +=1
        
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            
            show_correct('Неправильно') 
    window.raiting = (window.true / window.total) * 100

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана


def test():
    ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
    show_result() либо show_question() '''
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()


def next_question():
    window.total +=1
    window.cur_question = window.cur_question + 1
    window.cur_question= randint(0, len(question_list))
    print('Статистика \n Всего вопросов:', window.total, '\n Всего правильно:', window.true, '\n Рейтинг:', window.raiting, '%')
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)


def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

mul3 = Question('Как звали главного злодея в мультсериале "Герои энвелла"', 'Моргарт', 'Черномор', 'Фрайк', 'Ванден')
mul2 = Question('Как звали одного из героев мультсериала "Герои энвелла", который играл за класс - рыцарь?', 'Артём', 'Филипп', 'Виктор', 'Дмитрий')
mul = Question('Как звали хозяйку главного героя в мультфильме "Вольт"?', 'Пенни', 'Клара', 'Кэра', 'Алекс')
che2 = Question('В каком году начался второй Чеченский кофликт?', '1999', '1998', '1997', '2000')
co = Question('В каком году Россия вступила в ЕСПЧ (Европейский союз по правам человека)?', '1998', '1997', '1999', '1993')
f = Question('Когда в России отменили смертную казнь (не временную отмену)', '1997', '1998', '1993','1994')
che = Question('Когда начался первый Чеченский конфликт?', '1994', '1996', '1993', '1991') 
ris = Question('Какая страна вышла последняя из СССР?', 'Казахстан', 'Украина', 'Беларусь', 'Россия')        
rus = Question('В каком году распался СССР?', '1991', '1990', '1992', '1989')
sh = Question('Вопрос для отдыха: Какое было ФИО у Шалтая-Болтая в фильме "Кот в сапогах"', 'Шалтай Александрович болтай', 'Шалтай Григорьевич Болтай', 'Шалтай Перекати Яйцевич', 'Шалтай Саламонавич Болтаевич')
m = Question('В каком году к власти в России пришли большевики?', '1917', '1991', '1922', '1920')
w = Question('В каком году в России была свергнута монархия?', '1917', '1914', '1991', '1918')
n = Question('Как в экономике называются средства, необходимые для удовлетворения потребности людей и имеющиеся в обществе в ограниченном количестве?', 'благо', 'товар', 'деньги', 'услуга')
c = Question('Когда началась Афганская война (более широкое название "Афган")', '1979', '1989', '1968', '1978')
l = Question('Как называется радикальное изменение всего строя государства?','революция','референдум', 'выборы', 'модернизация')
i = Question("Когда появился СССР?", "1922", '1920', '1924', '1918')
k = Question("Когда умер Ленин?", '1924', '1922', '1920', '1918')
b = Question('Когда умер Иосиф Сталин?', '1953', '1952', '1951', '1950')

question_list.append(mul3)
question_list.append(mul2)
question_list.append(mul)
question_list.append(che2)
question_list.append(co)
question_list.append(f)
question_list.append(che)
question_list.append(ris)
question_list.append(rus)
question_list.append(sh)
question_list.append(m)
question_list.append(w)
question_list.append(n)
question_list.append(c)
question_list.append(b)
question_list.append(k)
question_list.append(i)
question_list.append(l)
#shuffle(question_list)


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = -1
window.total = 0
window.true = 0
window.raiting = 0
show_correct('Правильно:')
next_question()

btn_OK.clicked.connect(click_ok) # проверяем, что панель ответов показывается при нажатии на кнопку
window.show()
app.exec()
