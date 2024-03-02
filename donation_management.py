# Import necessary library
import pandas as pd
from datetime import datetime

# Initialize donation records and distribution records as lists of dictionaries
donation_records = []
distribution_records = []

def register_donation(donor_name, donation_type, quantity, donation_date):
    """Registers a new donation."""
    donation_records.append({
        'Donor Name': donor_name,
        'Donation Type': donation_type,
        'Quantity': quantity,
        'Date': donation_date
    })

def distribute_donation(donation_type, quantity, distribution_date):
    """Logs the distribution of donations."""
    distribution_records.append({
        'Donation Type': donation_type,
        'Quantity': quantity,
        'Date': distribution_date
    })

def generate_inventory_report():
    """Generates an inventory report of current donation status, grouped by type."""
    df = pd.DataFrame(donation_records)
    distribution_df = pd.DataFrame(distribution_records)
    summary = df.groupby('Donation Type')['Quantity'].sum() - distribution_df.groupby('Donation Type')['Quantity'].sum()
    print("Inventory Report:")
    print(summary)

def generate_donator_report():
    """Generates a report summarizing total contributions received from each donor."""
    df = pd.DataFrame(donation_records)
    summary = df.groupby('Donor Name')['Quantity'].sum()
    print("Donator Report:")
    print(summary)

# Example usage
register_donation('John Doe', 'Money', 100, datetime.now().date())
register_donation('Jane Smith', 'Food', 50, datetime.now().date())
distribute_donation('Food', 20, datetime.now().date())

# Generating reports
generate_inventory_report()
generate_donator_report()
