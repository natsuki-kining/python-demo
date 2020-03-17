"""
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。



示例 1：

输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
示例 2：

输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
所有字符串中都仅包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
"""
words = ["cat", "bt", "hat", "tree"]
chars = "atach"


# 53 1
def count_characters(words, chars):
    know = 0
    for word in words:
        keep_chars = chars[:]
        for i in word:
            if i in keep_chars:
                keep_chars = keep_chars.replace(i, "", 1)
            else:
                break
        else:
            know += len(word)
    return know


print(count_characters(words, chars))

# 53 2
import collections


def count_characters_2(words, chars):
    ans = 0
    # Counter类计数器 # Counter({'a': 2, 't': 1, 'c': 1, 'h': 1})
    cnt = collections.Counter(chars)
    for w in words:
        # Counter({'c': 1, 'a': 1, 't': 1})
        c = collections.Counter(w)
        # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
        if all([c[i] <= cnt[i] for i in c]):
            ans += len(w)
    return ans


print(count_characters_2(words, chars))



#============================ 2520 ms	13.9 MB 跟53的相比差了20多倍，我太菜了 ==============

def count_characters_3(words, chars):
    length = 0
    tup_c = tuple(chars[:])
    for word in words:
        tup_w = tuple(word[:])
        count = 0
        word_length = len(word)

        for w in word:
            if(tup_c.count(w) >= tup_w.count(w)):
                count += 1

        if(count == word_length):
            length += word_length

    return length


print(count_characters_3(words, chars))


# 先统计各个字符才个数，再比较 比53大佬慢4倍左右 408 ms	13.7 MB
def count_characters_4(words, chars):
    length = 0
    dictionary_char = get_dictionary(chars)
    for word in words:
        dictionary_word = get_dictionary(word)
        count = 0
        word_length = len(word)

        for w in word:
            if(dictionary_char.get(w,0) >= dictionary_word.get(w,0)):
                count += 1

        if(count == word_length):
            length += word_length

    return length

def get_dictionary(chars):
    dictionary_char = {}
    for c in chars:
        count = dictionary_char.get(c,0)
        if(count == 0) :
            dictionary_char[c] = 1
        else:
            count += 1
            dictionary_char[c] = count
    return dictionary_char;

print(count_characters_4(words, chars))
