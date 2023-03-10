# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import QApplication,QMenuBar
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
import sys
import random
from PySide6 import QtCore, QtWidgets
from math import *
from rule_1 import *

class MyWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # 设置标题
        self.setWindowTitle("成绩转换")
        self.resize(800, 600)

#女子青年一组（25岁以下，含学员组）跳远 标准
        self.female_low_25_jump_range_dict = {floor(float(format(x[0] / 0.02,".3f"))): x for x in rule_female_low_25_jump}
#女子青年一组（25岁以下，含学员组）跳远 标准

#男子青年一组（25岁以下，含学员组）跳远 标准
        self.male_low_25_jump_range_dict = {floor(float(format(x[1] / 0.02,".3f"))): x for x in rule_male_low_25_jump}
#男子青年一组（25岁以下，含学员组）跳远 标准


#女子青年一组（25岁以下，含学员组）4*10 标准
        self.female_low_25_4_10_range_dict = {trunc(x[1] / 0.3): x for x in rule_female_low_25_4_10}
#女子青年一组（25岁以下，含学员组）4*10 标准

#男子青年一组（25岁以下，含学员组）4*10 标准
        self.male_low_25_4_10_range_dict = {float(format((x[1] - 0.2) / 0.3,'.3f')): x for x in rule_male_low_25_4_10}
#男子青年一组（25岁以下，含学员组）4*10 标准

#女子青年一组（25岁以下，含学员组）1分钟仰卧起坐 标准
        self.female_low_25_1_min_wo_range_dict = {trunc(x[1] //2): x for x in rule_female_low_25_1_min_wo}
#女子青年一组（25岁以下，含学员组）1分钟仰卧起坐 标准

#女子青年一组（25岁以下，含学员组）800m跑步 标准
        self.female_low_25_800m_range_dict_1 = {float(format((x[1]+1) / 3,'.3f')): x for x in rule_female_low_25_800m_1}
        self.female_low_25_800m_range_dict_2 = {float(format((x[0] / 5)+1,'.3f')): x for x in rule_female_low_25_800m_2}
#女子青年一组（25岁以下，含学员组）800m跑步 标准

#男子青年一组（25岁以下，含学员组）1000m跑步 标准
        self.male_low_25_1000m_range_dict_1 = {float(format((x[1]) / 2,'.3f')): x for x in rule_male_low_25_1000m_1}
        self.male_low_25_1000m_range_dict_2 = {float(format(((x[0]+1) / 3),'.3f')): x for x in rule_male_low_25_1000m_2}
        self.male_low_25_1000m_range_dict_3 = {float(format((x[0] / 5)+1,'.3f')): x for x in rule_male_low_25_1000m_3}
#男子青年一组（25岁以下，含学员组）1000m跑步 标准


        tab_widget = QTabWidget(self)


#女子青年一组（25岁以下，含学员组）跳远
        widget_form_female_low_25_jump = QWidget()
        self.female_low_25_jump_grade_1 = QTextEdit()
        self.female_low_25_jump_grade_2 = QTextEdit()

        button_female_low_25_jump = QPushButton("女生 跳远成绩转换")
        button_female_low_25_jump.clicked.connect(self.button_female_low_25_jump)
        # 添加布局
        form_layout_female_low_25_jump = QHBoxLayout()
        form_layout_female_low_25_jump.addWidget(self.female_low_25_jump_grade_1)
        form_layout_female_low_25_jump.addWidget(button_female_low_25_jump)
        form_layout_female_low_25_jump.addWidget(self.female_low_25_jump_grade_2)
        widget_form_female_low_25_jump.setLayout(form_layout_female_low_25_jump)
#女子青年一组（25岁以下，含学员组）跳远

#男子青年一组（25岁以下，含学员组）跳远
        widget_form_male_low_25_jump = QWidget()
        self.male_low_25_jump_grade_1 = QTextEdit()
        self.male_low_25_jump_grade_2 = QTextEdit()

        button_male_low_25_jump = QPushButton("男生 跳远成绩转换")
        button_male_low_25_jump.clicked.connect(self.button_male_low_25_jump)
        # 添加布局
        form_layout_male_low_25_jump = QHBoxLayout()
        form_layout_male_low_25_jump.addWidget(self.male_low_25_jump_grade_1)
        form_layout_male_low_25_jump.addWidget(button_male_low_25_jump)
        form_layout_male_low_25_jump.addWidget(self.male_low_25_jump_grade_2)
        widget_form_male_low_25_jump.setLayout(form_layout_male_low_25_jump)
#男子青年一组（25岁以下，含学员组）跳远



#女子青年一组（25岁以下，含学员组）4*10
        widget_form_female_low_25_4_10 = QWidget()
        self.female_low_25_4_10_edit_1 = QTextEdit()
        self.female_low_25_4_10_edit_2 = QTextEdit()

        button_female_low_25_4_10 = QPushButton("女生 4*10成绩转换")
        button_female_low_25_4_10.clicked.connect(self.button_female_low_25_4_10)
        # 添加布局
        form_layout_female_low_25_4_10 = QHBoxLayout()
        form_layout_female_low_25_4_10.addWidget(self.female_low_25_4_10_edit_1)
        form_layout_female_low_25_4_10.addWidget(button_female_low_25_4_10)
        form_layout_female_low_25_4_10.addWidget(self.female_low_25_4_10_edit_2)
        widget_form_female_low_25_4_10.setLayout(form_layout_female_low_25_4_10)
#女子青年一组（25岁以下，含学员组）4*10

#男子青年一组（25岁以下，含学员组）4*10
        widget_form_male_low_25_4_10 = QWidget()
        self.male_low_25_4_10_edit_1 = QTextEdit()
        self.male_low_25_4_10_edit_2 = QTextEdit()

        button_male_low_25_4_10 = QPushButton("男生 4*10成绩转换")
        button_male_low_25_4_10.clicked.connect(self.button_male_low_25_4_10)
        # 添加布局
        form_layout_male_low_25_4_10 = QHBoxLayout()
        form_layout_male_low_25_4_10.addWidget(self.male_low_25_4_10_edit_1)
        form_layout_male_low_25_4_10.addWidget(button_male_low_25_4_10)
        form_layout_male_low_25_4_10.addWidget(self.male_low_25_4_10_edit_2)
        widget_form_male_low_25_4_10.setLayout(form_layout_male_low_25_4_10)
#男子青年一组（25岁以下，含学员组）4*10



#女子青年一组（25岁以下，含学员组）800米跑步
        widget_form_female_low_25_800m = QWidget()
        self.female_low_25_800m_edit1 = QTextEdit()
        self.female_low_25_800m_edit2 = QTextEdit()

        button_female_low_25_800m = QPushButton("女生 800米跑步成绩转换")
        button_female_low_25_800m.clicked.connect(self.button_female_low_25_800m)
        # 添加布局
        form_layout_female_low_25_800m = QHBoxLayout()
        form_layout_female_low_25_800m.addWidget(self.female_low_25_800m_edit1)
        form_layout_female_low_25_800m.addWidget(button_female_low_25_800m)
        form_layout_female_low_25_800m.addWidget(self.female_low_25_800m_edit2)
        widget_form_female_low_25_800m.setLayout(form_layout_female_low_25_800m)
#女子青年一组（25岁以下，含学员组）800米跑步

#男子青年一组（25岁以下，含学员组）1000m跑步
        widget_form_male_low_25_1000m = QWidget()
        self.male_low_25_1000m_edit1 = QTextEdit()
        self.male_low_25_1000m_edit2 = QTextEdit()

        button_male_low_25_1000m = QPushButton("男生 1000米跑步成绩转换")
        button_male_low_25_1000m.clicked.connect(self.button_male_low_25_1000m)
        # 添加布局
        form_layout_male_low_25_1000m = QHBoxLayout()
        form_layout_male_low_25_1000m.addWidget(self.male_low_25_1000m_edit1)
        form_layout_male_low_25_1000m.addWidget(button_male_low_25_1000m)
        form_layout_male_low_25_1000m.addWidget(self.male_low_25_1000m_edit2)
        widget_form_male_low_25_1000m.setLayout(form_layout_male_low_25_1000m)
#男子青年一组（25岁以下，含学员组）1000m跑步



#女子青年一组（25岁以下，含学员组）1分钟仰卧起坐
        widget_form_female_low_25_1_min_wo = QWidget()
        self.female_low_25_1_min_wo_edit_1 = QTextEdit()
        self.female_low_25_1_min_wo_edit_2 = QTextEdit()

        button_female_low_25_1_min_wo = QPushButton("女生 1分钟仰卧起坐成绩转换")
        button_female_low_25_1_min_wo.clicked.connect(self.button_female_low_25_1_min_wo)
        # 添加布局
        form_layout_female_low_25_1_min_wo = QHBoxLayout()
        form_layout_female_low_25_1_min_wo.addWidget(self.female_low_25_1_min_wo_edit_1)
        form_layout_female_low_25_1_min_wo.addWidget(button_female_low_25_1_min_wo)
        form_layout_female_low_25_1_min_wo.addWidget(self.female_low_25_1_min_wo_edit_2)
        widget_form_female_low_25_1_min_wo.setLayout(form_layout_female_low_25_1_min_wo)
#女子青年一组（25岁以下，含学员组）1分钟仰卧起坐




        #总成绩转换
        all_grade = QWidget()
        button_all_grade = QPushButton("总成绩转换")
        buttons_layout = QVBoxLayout()

        buttons_layout.addWidget(button_all_grade)
        all_grade.setLayout(buttons_layout)
        #总成绩转换


        #Add tabs to widget
        tab_widget.addTab(widget_form_female_low_25_jump,"女子青年一组（25岁以下，含学员组）跳远") # ok
        tab_widget.addTab(widget_form_male_low_25_jump,"男子青年一组（25岁以下，含学员组）跳远") # ok
        tab_widget.addTab(widget_form_female_low_25_4_10,"女子青年一组（25岁以下，含学员组）4*10")
        tab_widget.addTab(widget_form_male_low_25_4_10,"男子青年一组（25岁以下，含学员组）4*10")
        tab_widget.addTab(widget_form_female_low_25_800m,"女子青年一组（25岁以下，含学员组）800米跑")
        tab_widget.addTab(widget_form_male_low_25_1000m,"男子青年一组（25岁以下，含学员组）1000m跑步")
        tab_widget.addTab(widget_form_female_low_25_1_min_wo,"女子青年一组（25岁以下，含学员组）1分钟仰卧起坐") # ok
        tab_widget.addTab(all_grade,"总成绩转换")
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)


#女子青年一组（25岁以下，含学员组）4*10 button
    def button_female_low_25_4_10(self):
        self.female_low_25_4_10_edit_2.setPlainText("")
        tra1 = self.female_low_25_4_10_edit_1.toPlainText()
        tmp_r1 = ""
        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                i = float(i)
                if i <= 10.20:
                    tmp_r1 += "满分\n"
                    continue
                if i > 14.10:
                   tmp_r1 += "不及格\n"
                   continue
                po = self.female_low_25_4_10_range_dict.get(ceil(float(format(i/0.3,'.3f'))))
                print(f"考生跳远距离: {i} 米,范围:{po},最终得分:{po[-1]}")
                tmp_r1 += f"{po[-1]}分\n"
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.female_low_25_4_10_edit_2.setPlainText(tmp_r1)
#女子青年一组（25岁以下，含学员组）4*10 button

#男子青年一组（25岁以下，含学员组）4*10 button
    def button_male_low_25_4_10(self):
        self.male_low_25_4_10_edit_2.setPlainText("")
        tra1 = self.male_low_25_4_10_edit_1.toPlainText()
        tmp_r1 = ""
        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                i = float(i)
                if i <= 9.2:
                    tmp_r1 += "满分\n"
                    continue
                if i > 13.1:
                   tmp_r1 += "不及格\n"
                   continue
                po = self.male_low_25_4_10_range_dict.get(ceil(float(format((i - 0.2) / 0.3,".3f"))))
                print(f"考生跳远距离: {i} 米,范围:{po},最终得分:{po[-1]}")
                tmp_r1 += f"{po[-1]}分\n"
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.male_low_25_4_10_edit_2.setPlainText(tmp_r1)
#男子青年一组（25岁以下，含学员组）4*10 button



#女子青年一组（25岁以下，含学员组）800米跑步 button
    def button_female_low_25_800m(self):
        self.female_low_25_800m_edit2.setPlainText("")
        tra1 = self.female_low_25_800m_edit1.toPlainText()
        tmp_r1 = ""

        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                r1 = float(i.split(".")[0])*60 + float(i.split(".")[1])
                i = float(r1)
                # print(i)
                if i <= 203:
                    tmp_r1 += "满分\n"
                    continue
                if i > 260:
                    tmp_r1 += "不及格\n"
                    continue
                if i > 215:
                    po1 = self.female_low_25_800m_range_dict_2.get(ceil(float(format((i) / 5,".3f"))))
                    tmp_r1 += f"{po1[-1]}分\n"
                    continue
                else:
                    po2 = self.female_low_25_800m_range_dict_1.get(ceil(float(format((i+1) / 3,".3f"))))
                    tmp_r1 += f"{po2[-1]}分\n"
                    continue
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.female_low_25_800m_edit2.setPlainText(tmp_r1)
#女子青年一组（25岁以下，含学员组）800米跑步 button


#男子青年一组（25岁以下，含学员组）1000m跑步 button
    def button_male_low_25_1000m(self):
        self.male_low_25_1000m_edit2.setPlainText("")
        tra1 = self.male_low_25_1000m_edit1.toPlainText()
        tmp_r1 = ""

        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                r1 = float(i.split(".")[0])*60 + float(i.split(".")[1])
                i = float(r1)
                if i <= 206:
                    tmp_r1 += "满分\n"
                    continue
                if i > 260:
                    tmp_r1 += "不及格\n"
                    continue
                if i <= 212:
                    po1 = self.male_low_25_1000m_range_dict_1.get(ceil(float(format((i) / 2,".3f"))))
                    tmp_r1 += f"{po1[-1]}分\n"
                    continue
                if 215 >= i > 212:
                    po2 = self.male_low_25_1000m_range_dict_2.get(floor(float(format((i) / 3,".3f"))))
                    tmp_r1 += f"{po2[-1]}分\n"
                    continue
                if i > 215:
                    po2 = self.male_low_25_1000m_range_dict_3.get(ceil(float(format((i) / 5,".3f"))))
                    tmp_r1 += f"{po2[-1]}分\n"
                    continue
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.male_low_25_1000m_edit2.setPlainText(tmp_r1)
#男子青年一组（25岁以下，含学员组）1000m跑步 button



#女子青年一组（25岁以下，含学员组）1分钟仰卧起坐 button
    def button_female_low_25_1_min_wo(self):
        self.female_low_25_1_min_wo_edit_2.setPlainText("")
        tra1 = self.female_low_25_1_min_wo_edit_1.toPlainText()
        tmp_r1 = ""
        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                i = float(i)
                if i < 17:
                    tmp_r1 += "不及格\n"
                    continue
                if i >= 43:
                   tmp_r1 += "满分\n"
                   continue
                po = self.female_low_25_1_min_wo_range_dict.get(ceil(float(format(i/2,'.3f'))))
    #            print(f"考生跳远距离: {i} 米,范围:{po},最终得分:{po[-1]}")
                tmp_r1 += f"{po[-1]}分\n"
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.female_low_25_1_min_wo_edit_2.setPlainText(tmp_r1)
#女子青年一组（25岁以下，含学员组）1分钟仰卧起坐 button

#女子青年一组（25岁以下，含学员组）跳远 button
    def button_female_low_25_jump(self):
        self.female_low_25_jump_grade_2.setPlainText("")
        tra1 = self.female_low_25_jump_grade_1.toPlainText()
        tmp_r1 = ""
        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                i = float(i)
                if i < 1.58:
                    print(f"{i}米的距离不及格")
                    tmp_r1 += "不及格\n"
                    continue
                if i >= 2.10:
                   tmp_r1 += "满分\n"
                   continue
                po = self.female_low_25_jump_range_dict.get(floor(float(format(i / 0.02,".3f"))))
    #            print(f"考生跳远距离: {i} 米,范围:{po},最终得分:{po[-1]}")
                tmp_r1 += f"{po[-1]}分\n"
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.female_low_25_jump_grade_2.setPlainText(tmp_r1)
#女子青年一组（25岁以下，含学员组）跳远 button


#男子青年一组（25岁以下，含学员组）跳远 button
    def button_male_low_25_jump(self):
        self.male_low_25_jump_grade_2.setPlainText("")
        tra1 = self.male_low_25_jump_grade_1.toPlainText()
        tmp_r1 = ""
        for line,i in enumerate(tra1.split("\n")):
            if i != "":
                i = float(i)
                if i < 2.17:
                    print(f"{i}米的距离不及格")
                    tmp_r1 += "不及格\n"
                    continue
                if i >= 2.69:
                   tmp_r1 += "满分\n"
                   continue
                po = self.male_low_25_jump_range_dict.get(ceil(float(format(i / 0.02,".3f"))))
    #            print(f"考生跳远距离: {i} 米,范围:{po},最终得分:{po[-1]}")
                tmp_r1 += f"{po[-1]}分\n"
            else:
                QMessageBox.critical(self,"不要输入空行","第" + str(line+1) + "是空行", QMessageBox.Ok | QMessageBox.Cancel)
        self.male_low_25_jump_grade_2.setPlainText(tmp_r1)
#男子青年一组（25岁以下，含学员组）跳远 button



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget(app)
    window.setFont(QFont('Arial', 15, QFont.Bold))
    window.show()
    sys.exit(app.exec())
