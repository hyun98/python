class NotPalindromeError(Exception):
	pass

def palindrome(word):
	if word != word[::-1]:
		raise NotPalindromeError("회문이 아닙니다.")
	else:
		print(word)

if __name__ == "__main__":
	try:
		word = input()
		palindrome(word)
	except NotPalindromeError as e:
		print(e)
	