import signal
import time

class myapp:
	cleanup_now = False
	def __init__(self):
		signal.signal(signal.SIGTERM, self.exit_gracefully)

		# main logic loop
		while not self.cleanup_now:
			time.sleep(1)
			print("Still running smoothly")

		# code gets here once the SIGTERM breaks the main loop - time to clean up!
		print("Received SIGTERM!")
		print('''Now would be a good time to terminate database and network connections,
		dump state from memory to disk, and write something useful in the logs''')

	def exit_gracefully(self,signum, frame):
		self.cleanup_now = True

if __name__ == '__main__':
	app = myapp()

