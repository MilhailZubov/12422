with open('wew_2.txt',) as f:
    strs = f.readlines()
print('Количество строк:', len(strs))
for srt_123, str_321 in enumerate(strs, start=1):
    print('{} строка содерджит - {} слов(a)'.format(srt_123, len(str_321.split())))