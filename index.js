import { fetchExtensionZip } from 'chrome-extension-fetch';
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
const path = require('path');


(async () => {
    try {
        const { crxPath, zipPath } = await fetchExtensionZip(
            'https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc',
            {
                chromeVersion: '114.0.5735.133', // Optional: defaults to this version if not provided.
                outputDir: 'extensions' // Optional: defaults to "extensions"
            }
        );
        console.log('CRX saved at:', crxPath);
        console.log('ZIP saved at:', zipPath);
    } catch (error) {
        console.error('Failed to fetch extension:', error.message);
    }
})();



async function uploadFileToWebhook(filePath, webhookUrl) {
    try {
        // بررسی اینکه آیا فایل واقعاً وجود دارد
        if (!fs.existsSync(filePath)) {
            console.error(`Error: File not found at ${filePath} `);
            return;
        }

        console.log(`Starting upload: ${filePath} to ${webhookUrl}...`);

        // ایجاد یک فرم برای ارسال داده‌ها
        const form = new FormData();

        // اضافه کردن فایل به فرم
        // پارامتر اول نام فیلد است (مثلاً 'file')، پارامتر دوم مسیر فایل
        form.append('file', fs.createReadStream(filePath));

        // ارسال درخواست POST به وب‌هوک
        const response = await axios.post(webhookUrl, form, {
            headers: {
                ...form.getHeaders(), // این خط بسیار مهم است تا Headerهای مربوط به فرم درست ست شوند
            },
        });

        console.log('✅ Upload Successful!');
        console.log('Server Response:', response.data);

    } catch (error) {
        console.error('❌ Upload Failed!');
        if (error.response) {
            // اگر سرور پاسخ داده اما با کد خطا (مثل 404 یا 500)
            console.error('Response Data:', error.response.data);
            console.error('Status Code:', error.response.status);
        } else {
            // اگر خطای شبکه یا دیگری رخ داده باشد
            console.error('Error Message:', error.message);
        }
    }
}

// --- تنظیمات خودت را اینجا وارد کن ---
const MY_FILE_PATH = path.join(__dirname, 'extensions', 'get-cookiestxt-locally.crx');
const MY_WEBHOOK_URL = 'https://mmdaghaei.runflare.run/webhook/ef6241a8-68f3-40bf-a6f6-712482e45e1e'; // آدرس وب‌هوک خودت را اینجا بگذار

// اجرای تابع
uploadFileToWebhook(MY_FILE_PATH, MY_WEBHOOK_URL);
