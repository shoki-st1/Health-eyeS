import tkinter as tk

# 時間表示

# ボタンを押したときの判定


def setbutton_push():
    entered_text = int(timeset_text.get())
    if entered_text > 0:
        time_form.destroy()
    else:
        return


def form1_task():
    # グローバル変数で宣言
    # 時間入力のform
    global time_form
    global timeset_text
    time_form = tk.Tk()

    # ウィンドウのサイズ
    time_form.geometry('250x200')
    time_form.resizable(width=False, height=False)

    # 画面のタイトル
    time_form.title('時間を設定')

    # フォームのラベル
    timeset_label = tk.Label(text='時間を入力してください(分)')
    timeset_label.place(x=30, y=50)

    # 入力のテキストボックス
    timeset_text = tk.Entry(width=30)
    timeset_text.place(x=30, y=70)

    # 入力決定のボタン
    timeset_button = tk.Button(
        time_form,
        text='設定',
        command=setbutton_push
    ).place(x=100, y=150)

    # フォームのループ
    time_form.mainloop()
