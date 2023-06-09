from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.layouts import column
from bokeh.palettes import Category10_10
from bokeh.io import curdoc

# 创建数据
data = {
    '機械工程系': [598, 584, 580, 583, 521, 467],
    '電機工程系': [538, 517, 521, 537, 556, 557],
    '化學工程與生物科技系': [509, 498, 512, 521, 529, 553],
    '土木工程系': [419, 442, 460, 481, 464, 459],
    '電子工程系': [390, 393, 400, 417, 419, 437],
    '材料及資源工程系': [376, 380, 390, 412, 418, 417],
    '工業工程與管理系': [320, 324, 332, 328, 313, 338],
    '工業設計系': [277, 255, 282, 278, 263, 285],
    '互動設計系': [265, 288, 312, 307, 305, 300],
    '經營管理系': [234, 257, 272, 265, 247, 245]
}
years = [106, 107, 108, 109, 110, 111]

# 创建Bokeh图形对象
p = figure(title='系所學生數變化', x_axis_label='年度', y_axis_label='學生數', plot_width=800, plot_height=400)

# 创建ColumnDataSource对象
source = ColumnDataSource(data=dict(year=[], values=[]))

# 添加折线图
palette = Category10_10  # 颜色调色板
lines = []
for series, _ in data.items():
    line = p.line(x='year', y='values', source=source, line_color=palette[len(lines) % len(palette)], legend_label=series)
    lines.append(line)

# 设置图例位置
p.legend.location = 'top_left'

# 创建Slider控件
slider = Slider(start=0, end=len(years) - 1, value=0, step=1, title='年度')

# 定义JavaScript回调函数
callback = CustomJS(args=dict(source=source, slider=slider), code="""
    const yearIndex = slider.value;
    const data = source.data;
    const years = data['year'];
    const values = data['values'];
    
    // 更新数据
    values.length = 0;
    values.push(...data[String(yearIndex)]);
    years.length = 0;
    years.push(...Array.from({length: values.length}, (_, i) => i + 1));
    
    // 通知数据更新
    source.change.emit();
""")

# 绑定回调函数到Slider控件
slider.js_on_change('value', callback)

layout = column(slider, p)

# 创建文档并将布局添加到文档
doc = curdoc()
doc.add_root(layout)

# 在Jupyter Notebook中显示图形
show(layout)