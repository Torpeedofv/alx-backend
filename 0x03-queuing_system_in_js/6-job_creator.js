import kue from "kue";

const queue = kue.createQueue();
const jobData = {
	phoneNumber: "8146314687",
	message: "Account verification code",
};
const queueName= "push_notification_code";
const job = queue.create(queueName, jobData).save((err) => {
	if (!err) console.log(`Notification job created: ${job.id}`);
});
job.on("complete", () => {
	console.log("Notification job completed");
});

job.on("failed", () => {
	console.log("Notification job failed");
});
