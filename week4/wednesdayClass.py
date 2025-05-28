# 26th Feb, 2025 - Wednesday Class.

# LISTS AND DICTIONARIES

# Reverse does not work without the sort()
# You first sort, before you reverse, else, the items just reverses without any form of arrangements(sorting) been done.

menuList = ["Pineapple", "Apple", "Milk", "Milo", "Biscuit"]
#
# # def traverseList(menuList):
# #     for items in menuList:
# #         print(items)
# # traverseList(menuList)
#
#
# def sortList(menuList):
#     # newSortedList = menuList.sort()
#     # return newSortedList
#     menuList.sort()
#     print(menuList)
#
# sortList(menuList)
#
# def reverseList(menuList):
#     # reversedList = menuList.reverse()
#     # return reversedList
#     menuList.reverse()
#     print(menuList)
#
# reverseList(menuList)

def appendList(menuList):
    item = input("Enter your items to the menu list: ")
    menuList.append(item)
    return menuList

print(appendList(menuList))