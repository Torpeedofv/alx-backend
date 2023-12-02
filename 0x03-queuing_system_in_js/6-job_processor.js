import kue from "kue";

const queue = kue.createQueue();
function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

const queueCode = "push_notification_code";
queue.process(queueCode, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message);
	done();
});
