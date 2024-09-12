import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


class PlotDrawer:
    def __init__(self):
        self.plots_folder = 'plots'
        # Создаем папку для графиков, если её нет
        if not os.path.exists(self.plots_folder):
            os.makedirs(self.plots_folder)

    def draw_plots(self, json_path):
        # Чтение данных из JSON файла
        data = pd.read_json(json_path)

        # Используем названия комнат из столбца room_name, если они есть
        if 'name' in data.columns:
            room_names = data['name']
        else:
            # Если названий нет, генерируем вымышленные
            room_names = [f'Room {i + 1}' for i in range(len(data))]

        # Построение графиков для каждого столбца, кроме Gt_corners и Rb_corners
        columns_to_plot = ['mean', 'max', 'min', 'floor_mean',
                           'floor_max', 'floor_min', 'ceiling_mean',
                           'ceiling_max', 'ceiling_min']

        for column in columns_to_plot:
            plt.figure(figsize=(100, 20))  # Увеличиваем размер графика

            # Построение графика с помощью seaborn
            sns.barplot(x=room_names, y=column, data=data)

            # Поворот подписей на оси X для читаемости
            plt.xticks(rotation=90, ha='right', fontsize=7)  # Можно увеличить шрифт, если необходимо

            # Настройка подписей и заголовков
            plt.xlabel('Room Name')
            plt.ylabel(column)
            plt.title(f'{column} per Room')

            # Подгонка элементов графика для избежания наложений
            plt.tight_layout()

            # Сохранение графика
            plot_path = os.path.join(self.plots_folder, f"{column}_vs_room_name.png")
            plt.tight_layout()
            plt.savefig(plot_path)

        # Возвращаем список сохранённых графиков
        return os.listdir(self.plots_folder)

if __name__ == '__main__':
    # Создаем объект и строим графики
    drawer = PlotDrawer()
    drawer.draw_plots('deviation.json')
