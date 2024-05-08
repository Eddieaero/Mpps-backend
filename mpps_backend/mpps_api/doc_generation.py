from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_transit_pass(transit_pass):
    user = transit_pass.user
    business_license = transit_pass.business_license

    c = canvas.Canvas("TransitPass.pdf", pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 24)
    c.drawString(30, height - 50, "Transit Pass")

    c.setFont("Helvetica", 14)
    c.drawString(30, height - 100, f"User: {user.username}")
    c.drawString(30, height - 120, f"Company: {user.company_name}")
    c.drawString(30, height - 140, f"Phone: {user.phone_number}")
    c.drawString(30, height - 160, f"Address: {user.address}")

    c.drawString(30, height - 200, f"Business License: {business_license.license_number}")
    c.drawString(30, height - 220, f"Business Name: {business_license.business_name}")

    c.drawString(30, height - 260, f"Transit Pass ID: {transit_pass.transit_pass_id}")
    c.drawString(30, height - 280, f"Start Point: {transit_pass.start_point}")
    c.drawString(30, height - 300, f"End Point: {transit_pass.end_point}")
    c.drawString(30, height - 320, f"Start Date: {transit_pass.start_date}")
    c.drawString(30, height - 340, f"End Date: {transit_pass.end_date}")

    c.save()