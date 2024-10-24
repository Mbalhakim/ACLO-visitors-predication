import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'Data/Check-in times/Check-in-times_sheet_2017-2018.csv'
data = pd.read_csv(file_path)
# print(data.columns)
# Clean the data
# Removing rows where 'Klant nr' or other relevant fields are missing
data = data.dropna(subset=['Klant nr', 'Lid id', 'Geslacht', 'Abo bezoek', 'Incheckdatum'])

# Convert the 'Incheckdatum' to datetime
data['Incheckdatum'] = pd.to_datetime(data['Incheckdatum'], format='%Y-%m-%d %H:%M:%S')

# Let's extract useful time features like day, hour, and weekday
data['Day'] = data['Incheckdatum'].dt.date
data['Hour'] = data['Incheckdatum'].dt.hour
data['Weekday'] = data['Incheckdatum'].dt.weekday  # 0=Monday, 6=Sunday

# 1. Time Series Visualization - Check-ins over time
plt.figure(figsize=(10, 6))
data.groupby('Day').size().plot(kind='line', title='Check-ins over Time')
plt.ylabel('Number of Check-ins')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Hourly Check-in Patterns
plt.figure(figsize=(10, 6))
sns.countplot(data['Hour'])
plt.title('Hourly Check-in Distribution')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Check-ins')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Check-in Distribution by Membership Type (Abo bezoek)
plt.figure(figsize=(10, 6))
sns.countplot(y='Abo bezoek', data=data)
plt.title('Distribution of Check-ins by Membership Type')
plt.xlabel('Number of Check-ins')
plt.ylabel('Membership Type')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data['Geslacht'])
plt.title('Check-ins by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Check-ins')
plt.grid(True)
plt.tight_layout()
plt.show()
