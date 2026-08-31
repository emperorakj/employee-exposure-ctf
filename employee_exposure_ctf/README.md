# Employee Exposure

An employee directory exposes more information than intended. Find a way into the administrator area and recover the flag.

`difficulty: Medium` <br>
`author: Aryan`

## Flag
```text
EH4X{1D0R_l34k5_m0r3_th4n_y0u_th1nk}
```

## Solution

The public profile API does not verify whether a requester is authorized to access another employee's profile. Enumerating profile IDs reveals the administrator profile and a leaked password-reset token. Using that token at the admin recovery page grants access to the admin panel, where the flag is displayed.
