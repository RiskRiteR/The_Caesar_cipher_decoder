operating_mode = input('Создать шифр или дешифровать текст?(ш/д) ')
ru_eng = input('Русский или английский текст?(р/а) ')
cipher_step = input('? или шаг сдвига: ')
input_text = input('Введите текст: ')

if operating_mode == 'ш':
    if ru_eng == 'р':
        code_list = []
        for i in input_text:
            if 1071 >= ord(i) >= 1040 or 1103 >= ord(i) >= 1072:
                code = ord(i) + int(cipher_step)
                if code > 1071 and ord(i) <= 1071 or code > 1103 and ord(i) >= 1072:
                    code -= 32
            else:
                code = ord(i)
            code_list.append(chr(code))
        print(''.join(code_list))
    else:
        code_list = []
        for j in input_text:
            if 90 >= ord(j) >= 65 or 122 >= ord(j) >= 97:
                code = ord(j) + int(cipher_step)
                if code > 90 and ord(j) <= 90 or code > 122 and ord(j) >= 97:
                    code -= 26
            else:
                code = ord(j)
            code_list.append(chr(code))
        print(''.join(code_list))
else:
    if cipher_step == '?' and ru_eng == 'р':
        counter = 1
        while counter < 32:
            decoder_lists = []
            for _ in input_text:
                decoder = ord(_) - counter
                if 1071 >= ord(_) >= 1040 or 1103 >= ord(_) >= 1072:
                    if decoder < 1040 and ord(_) <= 1071 or decoder < 1072 and ord(_) >= 1072:
                        decoder += 32
                else:
                    decoder = ord(_)
                decoder_lists.append(chr(decoder))
            print(counter, ''.join(decoder_lists))
            counter += 1
    elif cipher_step == '?' and ru_eng == 'а':
        counter = 1
        while counter < 26:
            decoder_lists = []
            for _ in input_text:
                decoder = ord(_) - counter
                if 90 >= ord(_) >= 65 or 122 >= ord(_) >= 97:
                    if decoder < 65 and ord(_) <= 90 or decoder < 97 and ord(_) >= 97:
                        decoder += 26
                else:
                    decoder = ord(_)
                decoder_lists.append(chr(decoder))
            print(counter, ''.join(decoder_lists))
            counter += 1
    else:
        if ru_eng == 'р':
            decoder_list = []
            for k in input_text:
                decoder = ord(k) - int(cipher_step)
                if 1071 >= ord(k) >= 1040 or 1103 >= ord(k) >= 1072:
                    if decoder < 1040 and ord(k) <= 1071 or decoder < 1072 and ord(k) >= 1072:
                        decoder += 32
                else:
                    decoder = ord(k)
                decoder_list.append(chr(decoder))
            print(''.join(decoder_list))
        else:
            decoder_list = []
            for k2 in input_text:
                decoder = ord(k2) - int(cipher_step)
                if 90 >= ord(k2) >= 65 or 122 >= ord(k2) >= 97:
                    if decoder < 65 and ord(k2) <= 90 or decoder < 97 and ord(k2) >= 97:
                        decoder += 26
                else:
                    decoder = ord(k2)
                decoder_list.append(chr(decoder))
            print(''.join(decoder_list))
