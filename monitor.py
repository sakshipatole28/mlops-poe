from sklearn import datasets
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

iris = datasets.load_iris(as_frame=True).frame
reference = iris.iloc[:75]    # "old" data the model was trained on
current = iris.iloc[75:]      # "new" data arriving in production

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)
report.save_html("evidently_report.html")
print("Report saved: evidently_report.html")
