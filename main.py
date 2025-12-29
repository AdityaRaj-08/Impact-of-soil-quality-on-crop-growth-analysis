import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Impact-of-soil-quality-on-crop-growth-analysis/Crop_recommendation.csv")

print("csv loaded successfully")

print(df.head())

print(df.info())

print(df.isnull().sum())

duplicates=df.duplicated().sum()
print("number of duplicate rows:",duplicates)

if duplicates>0:
    df.drop_duplicates(inplace=True)
    print("Duplicates remove.")
    print("new shape:",df.shape)
else:
    print("No duplicate found,dataset is clean.")
    
le=LabelEncoder()
df["label_encoded"] =le.fit_transform(df["label"])
print(df[["label","label_encoded"]].head())

num_cols= ["N","P","K","temperature","humidity","ph","rainfall"]
scaler=StandardScaler()
df[num_cols]=scaler.fit_transform(df[num_cols])
print("Scaling completed")


print(df.describe())


df.describe().T


numeric_df=df.select_dtypes(include=["float64","int64"])
corr_matrix=numeric_df.corr()
print(corr_matrix)


num_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

for col in num_cols:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=30, edgecolor='black')
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()
    
    
for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.show()
    
sns.pairplot(df[num_cols])
plt.show()


plt.figure(figsize=(10,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


plt.figure(figsize=(12,6))
sns.boxplot(x=df["label"], y=df["N"])
plt.xticks(rotation=90)
plt.title("Nitrogen levels by Crop")
plt.show()

sns.boxplot(x=df["label"], y=df["P"])
plt.xticks(rotation=90)
plt.title("Phosphorus levels by Crop")
plt.show()

plt.figure(figsize=(14,14))   
sns.boxplot(x=df["label"], y=df["K"])
plt.xticks(rotation=90)
plt.title("Potassium levels by Crop")
plt.show()


plt.figure(figsize=(10,6))

sns.scatterplot(
    x=df["N"], 
    y=df["P"], 
    hue=df["label"],              # color by crop type
    palette="tab20",              # 20 different colors
    s=70,                         # point size
    edgecolor="black"
)

plt.title("Scatter Plot: Nitrogen (N) vs Phosphorus (P) by Crop Type")
plt.xlabel("Nitrogen (N)")
plt.ylabel("Phosphorus (P)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # move legend outside
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(x=df["P"], y=df["K"], hue=df["label"], palette="tab20", s=70, edgecolor="black")
plt.title("Scatter Plot: P vs K by Crop Type")
plt.xlabel("Phosphorus (P)")
plt.ylabel("Potassium (K)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

plt.figure(figsize=(10,6))

sns.scatterplot(
    x=df["temperature"], 
    y=df["humidity"], 
    hue=df["label"], 
    palette="tab20",
    s=70,
    edgecolor="black"
)

plt.title("Scatter Plot: Temperature vs Humidity by Crop Type")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

plt.figure(figsize=(10,6))

sns.scatterplot(
    x=df["ph"], 
    y=df["rainfall"], 
    hue=df["label"], 
    palette="tab20",
    s=70,
    edgecolor="black"
)

plt.title("Scatter Plot: Soil pH vs Rainfall by Crop Type")
plt.xlabel("Soil pH")
plt.ylabel("Rainfall (mm)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()