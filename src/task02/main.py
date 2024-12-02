def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Line '{line}' is malformed. Expected 3 values, got {len(parts)}.")
                cat_id, name, age = parts
                cat_dict = {'id': cat_id, 'name': name, 'age': age}
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"The file at {path} was not found.")
        raise
    except IOError:
        print(f"An error occurred while reading the file at {path}.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
    return cats_list

print(get_cats_info('cats_file.txt'))