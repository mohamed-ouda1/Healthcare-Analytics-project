import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os
from datetime import datetime

# --- 1. Data Loading & Preparation ---
def load_data():
    df = pd.read_csv('data/clean_healthcare__dataset.csv')
    df = df[df['Billing Amount'] > 0]
    return df

# --- 2. Generate Visuals for the Report ---
def generate_visuals(df):
    if not os.path.exists('temp_images'):
        os.makedirs('temp_images')
    
    sns.set_theme(style="whitegrid")
    
    # Chart 1: Billing by Medical Condition
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Medical Condition', y='Billing Amount', estimator='mean', palette='viridis')
    plt.title('Average Billing Amount by Medical Condition')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('temp_images/billing_condition.png')
    plt.close()

    # Chart 2: Admission Type Distribution
    plt.figure(figsize=(8, 8))
    df['Admission Type'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Distribution of Admission Types')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('temp_images/admission_dist.png')
    plt.close()

# --- 3. Create PDF Report ---
class PDFReport(FPDF):
    def header(self):
        # Logo placeholder (using a simple rectangle or text if no logo file exists)
        self.set_font('Arial', 'B', 15)
        self.set_text_color(0, 51, 102) # Dark Blue
        self.cell(0, 10, 'Healthcare Analytics Executive Report', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.set_text_color(100)
        self.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M")}', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_report(df):
    pdf = PDFReport()
    pdf.add_page()
    
    # Executive Summary Section
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, '1. Executive Summary', 0, 1, 'L')
    pdf.ln(2)
    
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(0)
    total_patients = len(df)
    avg_billing = df['Billing Amount'].mean()
    total_revenue = df['Billing Amount'].sum()
    avg_stay = df['length_of_stay'].mean()
    
    summary_text = (
        f"This month, our network processed a total of {total_patients:,} patients. "
        f"The average billing amount per patient stands at ${avg_billing:,.2f}, "
        f"contributing to a total revenue of ${total_revenue:,.2f}. "
        f"The average length of stay recorded was {avg_stay:.1f} days."
    )
    pdf.multi_cell(0, 10, summary_text)
    pdf.ln(5)

    # Key Insights Section
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, '2. Financial & Operational Insights', 0, 1, 'L')
    pdf.ln(2)

    # Add Chart 1
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'A. Average Billing by Medical Condition', 0, 1, 'L')
    pdf.image('temp_images/billing_condition.png', x=15, w=180)
    pdf.ln(10)

    # Add Chart 2 (New Page for better layout)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'B. Patient Volume by Admission Type', 0, 1, 'L')
    pdf.image('temp_images/admission_dist.png', x=40, w=130)
    pdf.ln(10)

    # Conclusion
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, '3. Recommendations', 0, 1, 'L')
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(0)
    recommendations = (
        "- Monitor Emergency admission costs closely as they represent a high revenue stream but higher resource usage.\n"
        "- Optimize discharge processes for conditions with longer-than-average stays to improve bed turnover.\n"
        "- Further investigate hospitals with outlier billing amounts for potential billing errors or efficiency gains."
    )
    pdf.multi_cell(0, 10, recommendations)

    # Save PDF
    if not os.path.exists('reports'):
        os.makedirs('reports')
        
    report_name = f"reports/Healthcare_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    pdf.output(report_name)
    print(f"Report generated successfully: {report_name}")
    return report_name

# --- 4. Main Execution ---
if __name__ == "__main__":
    print("Starting automated report generation...")
    data = load_data()
    generate_visuals(data)
    report_file = create_pdf_report(data)
    
    # Cleanup temp images
    import shutil
    if os.path.exists('temp_images'):
        shutil.rmtree('temp_images')
        print("Temporary images cleaned up.")
