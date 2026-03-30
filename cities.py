graph = {
    'Delhi': {'Jaipur': 280, 'Lucknow': 550, 'Chandigarh': 250},
    'Jaipur': {'Delhi': 280, 'Ahmedabad': 660, 'Indore': 570},
    'Chandigarh': {'Delhi': 250, 'Amritsar': 230},
    'Lucknow': {'Delhi': 550, 'Varanasi': 320, 'Patna': 530},
    'Ahmedabad': {'Jaipur': 660, 'Mumbai': 530},
    'Indore': {'Jaipur': 570, 'Bhopal': 190, 'Mumbai': 580},
    'Bhopal': {'Indore': 190, 'Nagpur': 350},
    'Nagpur': {'Bhopal': 350, 'Hyderabad': 500},
    'Mumbai': {'Ahmedabad': 530, 'Indore': 580, 'Pune': 150},
    'Pune': {'Mumbai': 150, 'Hyderabad': 560},
    'Hyderabad': {'Nagpur': 500, 'Pune': 560, 'Bangalore': 570},
    'Bangalore': {'Hyderabad': 570, 'Chennai': 350},
    'Chennai': {'Bangalore': 350},
    'Varanasi': {'Lucknow': 320, 'Patna': 260},
    'Patna': {'Lucknow': 530, 'Varanasi': 260},
    'Amritsar': {'Chandigarh': 230}
}

heuristic = {
    'Delhi': 1400, 'Jaipur': 1100, 'Chandigarh': 1600,
    'Lucknow': 1300, 'Ahmedabad': 500, 'Indore': 400,
    'Bhopal': 700, 'Nagpur': 800, 'Mumbai': 0,
    'Pune': 150, 'Hyderabad': 700, 'Bangalore': 1000,
    'Chennai': 1200, 'Varanasi': 1500, 'Patna': 1600,
    'Amritsar': 1700
}