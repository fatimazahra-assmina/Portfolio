from flask import Flask, render_template, request, jsonify
import xlrd
from flask import session
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static', static_folder='static')



@app.route('/Home_Page')
def Home_Page():
    return render_template('Home Page.html')

@app.route('/Product_view')
def Product_view():
    return render_template('Product view.html')

@app.route('/Brainstorming')
def Brainstorming():
    return render_template('Brainstorming assistant page.html')

@app.route('/Market_sizing')
def Market_sizing():
    return render_template('Marketing Analysis - Market sizing.html')

@app.route('/longitudinal_analysis')
def longitudinal_analysis():
    return render_template('Marketing Analysis - Longitudinal analysis.html')

@app.route('/Competitive_analysis')
def Competitive_analysis():
    return render_template('Marketing analysis - Competitive Analysis.html')

@app.route('/Vendors_analysis')
def Vendors_analysis():
    return render_template('Marketing Analysis - Vendors Analysis.html')

@app.route('/Req_diag')
def Req_diag():
    return render_template('Req Diagram.html')

@app.route('/Biz_req')
def Biz_req():
    return render_template('Business req.html')

@app.route('/Final_conception')
def Final_conception():
    return render_template('Final Conception.html')

@app.route('/Profile')
def Profile():
    return render_template('Profile page.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/timeline_page')
def timeline_page():
    return render_template('Timeline page.html')

@app.route('/creativity_area')
def creativity_area():
    return render_template('Creativity area.html')

@app.route('/generate_meetings')
def generate_meetings():
    return render_template('Geenrate meetings.html')

@app.route('/picture/<path:filename>')
def get_picture(filename):
    return send_from_directory('venv/static', filename)


@app.route('/extract_info', methods=['POST'])
def extract_info():
    file = request.files['file']
    workbook = xlrd.open_workbook(file_contents=file.read())
    sheet = workbook.sheet_by_index(0)

    extracted_info = {}
    for row_num in range(sheet.nrows):
        for col_num in range(sheet.ncols):
            cell_value = sheet.cell_value(row_num, col_num)
            if cell_value == "Gross Margin %":
                gross_margin = sheet.cell_value(row_num, col_num + 2) if col_num + 2 < sheet.ncols else "N/A"
                extracted_info["Gross Margin %"] = gross_margin
            elif cell_value == "Proxy MARGIN %":
                proxy_margin = sheet.cell_value(row_num, col_num + 2) if col_num + 2 < sheet.ncols else "N/A"
                extracted_info["Proxy MARGIN %"] = proxy_margin
            elif cell_value == "PBT":
                pbt = sheet.cell_value(row_num, col_num + 2) if col_num + 2 < sheet.ncols else "N/A"
                extracted_info["PBT"] = pbt

    return jsonify(extracted_info)


if __name__ == '__main__':
    app.run(debug=True)

