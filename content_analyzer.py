import os
import re
from collections import defaultdict

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_keywords(text):
    # This is a basic keyword extraction. You might want to improve this.
    words = re.findall(r'\b\w+\b', text.lower())
    return [word for word in words if len(word) > 3]

def analyze_content(directory):
    content_map = defaultdict(list)
    
    for filename in os.listdir(directory):
        if filename.endswith('.md'):  # Changed to .md for Markdown files
            file_path = os.path.join(directory, filename)
            content = read_file(file_path)
            keywords = extract_keywords(content)
            
            for keyword in keywords:
                content_map[keyword].append(filename)
    
    return content_map

def find_similar_articles(content_map, threshold=5):
    similar_articles = []
    
    for keyword, articles in content_map.items():
        if len(articles) > 1:
            for i in range(len(articles)):
                for j in range(i+1, len(articles)):
                    pair = (articles[i], articles[j])
                    if pair not in similar_articles:
                        similar_articles.append(pair)
    
    return [pair for pair in similar_articles if len(set(content_map.keys()) & set(extract_keywords(read_file(os.path.join('articles', pair[0]))) & set(extract_keywords(read_file(os.path.join('articles', pair[1]))))) > threshold]

def main():
    directory = 'articles'  # Replace with the path to your articles
    content_map = analyze_content(directory)
    similar_articles = find_similar_articles(content_map)
    
    print("Potentially similar articles:")
    for article1, article2 in similar_articles:
        print(f"{article1} and {article2}")

if __name__ == "__main__":
    main()