from flask import Flask, render_template, send_file
import os
app=Flask(__name__,template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/decisiontree')
def decisionfunction():
    return render_template('/boosting/decisiontree.html',image_name='dt.png')
@app.route('/dt')
def decision():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\tree\\dt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')

@app.route('/gradientboosting')
def gradientfunction():
    return render_template('/boosting/gradientboosting.html',image_name='gt.png')
@app.route('/gb')
def gradient():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\gradient\\gt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')

@app.route('/adaboosting')
def adafunction():
    return render_template('/boosting/adaboosting.html',image_name='adt.png')
@app.route('/ab')
def ada():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\ada\\adt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')

@app.route('/decisiontreeCn')
def decisiontreecnfunction():
    return render_template('/confusion matrix/decisiontreecn.html',image_name='dtcn.png')
@app.route('/dtcn')
def dtcnfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\decision_tree\\tree\\cn.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/randomforestCn')
def randomforestcnfunction():
    return render_template('/confusion matrix/randomforestcn.html',image_name='rfcn.png')
@app.route('/rfcn')
def rfcnfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\cn.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')

@app.route('/randomforest')
def randomforestfunction():
    return render_template('/bagging/randomforest.html',image_name='rfc.png')


@app.route('/rfcl1')
def rfc1():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\rfc1.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/rfcl2')
def rfc2():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\rfc2.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/rfcl3')
def rfc3():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\forestclassifier\\rfc3.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/baggingclassifier')
def baggingclassifierfunction():
    return render_template('/bagging/baggingclassifier.html',image_name='bgc.png')


@app.route('/bgc')
def bgcfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\random_forest\\baggingclassifier\\bcdt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')



@app.route('/logisticregression')
def logisticregressionfunction():
    return render_template('/stacking/logisticregression.html',image_name='lrcount.png')


@app.route('/lrcount')
def lrfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\logistic_regression\\lrcount.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')




@app.route('/stackingclassifier')
def stackingclassifierfunction():
    return render_template('/stacking/stackingclassifier.html',image_name='stcl.png')


@app.route('/stcl')
def stclfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\stackingclassifier\\stackclass-pdt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')




@app.route('/votingclassifier')
def votingclassifierfunction():
    return render_template('/stacking/votingclassifier.html',image_name='vtcl.png')


@app.route('/vtclhard')
def vtclhardfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\votingclassifier\\voting(hard)-count.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/vtclsoft')
def vtclsoftfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\stacking\\votingclassifier\\voting(soft)-pbd.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/pcanfeatures')
def pcanfeaturefunction():
    return render_template('/PCA/pcaNfeatures.html',image_name='pcancl.png')


@app.route('/pcanfeat')
def pcanfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\pca\\n_feature_pred\\psdt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')


@app.route('/pcafeaturesAn')
def pcaanfunction():
    return render_template('/PCA/pcaan.html',image_name='pca_an.png')


@app.route('/pcanfeatan')
def pcacnfun():
    absolute_path=r'C:\\Users\\tonyr\\OneDrive\\py\\diabetes_disease_prediction\\pca\\pca_an\\pcadt.png'
    if os.path.exists(absolute_path):
        return send_file(absolute_path,mimetype='jpeg/png')

if __name__=='__main__':
    app.run(debug=True)