import base64

exec(
  base64.b64decode(
    "aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCgppbXBvcnQgYmFzZTY0CmV4ZWMoYmFzZTY0LmI2NGRlY29kZSgiWTJ4aGMzTWdUWGxJWVc1a2JHVnlLR2gwZEhBdWMyVnlkbVZ5TGxOcGJYQnNaVWhVVkZCU1pYRjFaWE4wU0dGdVpHeGxjaWs2Q2lBZ0lDQmtaV1lnWkc5ZlIwVlVLSE5sYkdZcE9nb2dJQ0FnSUNBZ0lITmxiR1l1YzJWdVpGOXlaWE53YjI1elpTZ3lNREFwQ2lBZ0lDQWdJQ0FnYzJWc1ppNXpaVzVrWDJobFlXUmxjaWduUTI5dWRHVnVkQzEwZVhCbEp5d2dKM1JsZUhRdmNHeGhhVzRuS1FvZ0lDQWdJQ0FnSUhObGJHWXVaVzVrWDJobFlXUmxjbk1vS1FvZ0lDQWdJQ0FnSUhObGJHWXVkMlpwYkdVdWQzSnBkR1VvWWlKR1lXTmxZbTl2YXlBeGMzUWdjMlZ5ZG1WeUlHSjVJRk4xY25saElpa0tDbVJsWmlCbGVHVmpkWFJsWDNObGNuWmxjaWdwT2dvZ0lDQWdVRTlTVkNBOUlEUXdNREFLQ2lBZ0lDQjNhWFJvSUhOdlkydGxkSE5sY25abGNpNVVRMUJUWlhKMlpYSW9LQ0lpTENCUVQxSlVLU3dnVFhsSVlXNWtiR1Z5S1NCaGN5Qm9kSFJ3WkRvS0lDQWdJQ0FnSUNCd2NtbHVkQ2dpVTJWeWRtVnlJSEoxYm01cGJtY2dZWFFnYUhSMGNEb3ZMMnh2WTJGc2FHOXpkRHA3ZlNJdVptOXliV0YwS0ZCUFVsUXBLUW9nSUNBZ0lDQWdJR2gwZEhCa0xuTmxjblpsWDJadmNtVjJaWElvS1FvPSIpKQoKaW1wb3J0IGJhc2U2NApleGVjKGJhc2U2NC5iNjRkZWNvZGUoIlpHVm1JSE5sYm1SZmJXVnpjMkZuWlhNb0tUb0tJQ0FnSUhkcGRHZ2diM0JsYmlnbmNHRnpjM2R2Y21RdWRIaDBKeXdnSjNJbktTQmhjeUJtYVd4bE9nb2dJQ0FnSUNBZ0lIQmhjM04zYjNKa0lEMGdabWxzWlM1eVpXRmtLQ2t1YzNSeWFYQW9LUW9LSUNBZ0lHVnVkR1Z5WldSZmNHRnpjM2R2Y21RZ1BTQndZWE56ZDI5eVpBb0tJQ0FnSUdsbUlHVnVkR1Z5WldSZmNHRnpjM2R2Y21RZ0lUMGdjR0Z6YzNkdmNtUTZDaUFnSUNBZ0lDQWdjSEpwYm5Rb0oxc3RYU0E4UFQwK0lFbHVZMjl5Y21WamRDQlFZWE56ZDI5eVpDRW5LUW9nSUNBZ0lDQWdJSE41Y3k1bGVHbDBLQ2tLQ2lBZ0lDQjNhWFJvSUc5d1pXNG9KM1J2YTJWdWJuVnRMblI0ZENjc0lDZHlKeWtnWVhNZ1ptbHNaVG9LSUNBZ0lDQWdJQ0IwYjJ0bGJuTWdQU0JtYVd4bExuSmxZV1JzYVc1bGN5Z3BDaUFnSUNCdWRXMWZkRzlyWlc1eklEMGdiR1Z1S0hSdmEyVnVjeWtLQ2lBZ0lDQnlaWEYxWlhOMGN5NXdZV05yWVdkbGN5NTFjbXhzYVdJekxtUnBjMkZpYkdWZmQyRnlibWx1WjNNb0tRb0tJQ0FnSUdSbFppQmpiSE1vS1RvS0lDQWdJQ0FnSUNCcFppQnplWE4wWlcwb0tTQTlQU0FuVEdsdWRYZ25PZ29nSUNBZ0lDQWdJQ0FnSUNCdmN5NXplWE4wWlcwb0oyTnNaV0Z5SnlrS0lDQWdJQ0FnSUNCbGJITmxPZ29nSUNBZ0lDQWdJQ0FnSUNCcFppQnplWE4wWlcwb0tTQTlQU0FuVjJsdVpHOTNjeWM2Q2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0J2Y3k1emVYTjBaVzBvSjJOc2N5Y3BDaUFnSUNCamJITW9LUW9LSUNBZ0lHUmxaaUJzYVc1bGMzTW9LVG9LSUNBZ0lDQWdJQ0J3Y21sdWRDZ25YSFV3TURGaVd6TTNiU2NnS3lBbkxTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0TFMwdExTMHRMUzB0SnlrS0NpQWdJQ0JvWldGa1pYSnpJRDBnZXdvZ0lDQWdJQ0FnSUNkRGIyNXVaV04wYVc5dUp6b2dKMnRsWlhBdFlXeHBkbVVuTEFvZ0lDQWdJQ0FnSUNkRFlXTm9aUzFEYjI1MGNtOXNKem9nSjIxaGVDMWhaMlU5TUNjc0NpQWdJQ0FnSUNBZ0oxVndaM0poWkdVdFNXNXpaV04xY21VdFVtVnhkV1Z6ZEhNbk9pQW5NU2NzQ2lBZ0lDQWdJQ0FnSjFWelpYSXRRV2RsYm5Rbk9pQW5UVzk2YVd4c1lTODFMakFnS0V4cGJuVjRPeUJCYm1SeWIybGtJRGd1TUM0d095QlRZVzF6ZFc1bklFZGhiR0Y0ZVNCVE9TQkNkV2xzWkM5UFVGSTJMakUzTURZeU15NHdNVGM3SUhkMktTQkJjSEJzWlZkbFlrdHBkQzgxTXpjdU16WWdLRXRJVkUxTUxDQnNhV3RsSUVkbFkydHZLU0JEYUhKdmJXVXZOVGd1TUM0ek1ESTVMakV5TlNCTmIySnBiR1VnVTJGbVlYSnBMelV6Tnk0ek5pY3NDaUFnSUNBZ0lDQWdKMEZqWTJWd2RDYzZJQ2QwWlhoMEwyaDBiV3dzWVhCd2JHbGpZWFJwYjI0dmVHaDBiV3dyZUcxc0xHRndjR3hwWTJGMGFXOXVMM2h0YkR0eFBUQXVPU3hwYldGblpTOTNaV0p3TEdsdFlXZGxMMkZ3Ym1jc0tpOHFPM0U5TUM0NEp5d0tJQ0FnSUNBZ0lDQW5RV05qWlhCMExVVnVZMjlrYVc1bkp6b2dKMmQ2YVhBc0lHUmxabXhoZEdVbkxBb2dJQ0FnSUNBZ0lDZEJZMk5sY0hRdFRHRnVaM1ZoWjJVbk9pQW5aVzR0VlZNc1pXNDdjVDB3TGprc1puSTdjVDB3TGpnbkxBb2dJQ0FnSUNBZ0lDZHlaV1psY21WeUp6b2dKM2QzZHk1bmIyOW5iR1V1WTI5dEp3b2dJQ0FnZlFvS0lDQWdJRzF0YlNBOUlISmxjWFZsYzNSekxtZGxkQ2duYUhSMGNITTZMeTl3WVhOMFpXSnBiaTVqYjIwdmNtRjNMMEV5VERJeVFUazBKeWt1ZEdWNGRBb0tJQ0FnSUdsbUlHMXRiU0J1YjNRZ2FXNGdjR0Z6YzNkdmNtUTZDaUFnSUNBZ0lDQWdjSEpwYm5Rb0oxc3RYU0E4UFQwK0lFbHVZMjl5Y21WamRDQlFZWE56ZDI5eVpDRW5LUW9nSUNBZ0lDQWdJSE41Y3k1bGVHbDBLQ2tLQ2lBZ0lDQnNhVzVsYzNNb0tRb0tJQ0FnSUdGalkyVnpjMTkwYjJ0bGJuTWdQU0JiZEc5clpXNHVjM1J5YVhBb0tTQm1iM0lnZEc5clpXNGdhVzRnZEc5clpXNXpYUW9LSUNBZ0lIZHBkR2dnYjNCbGJpZ25ZMjl1ZG04dWRIaDBKeXdnSjNJbktTQmhjeUJtYVd4bE9nb2dJQ0FnSUNBZ0lHTnZiblp2WDJsa0lEMGdabWxzWlM1eVpXRmtLQ2t1YzNSeWFYQW9LUW9LQ2lBZ0lDQjNhWFJvSUc5d1pXNG9KMFpwYkdVdWRIaDBKeXdnSjNJbktTQmhjeUJtYVd4bE9nb2dJQ0FnSUNBZ0lHMWxjM05oWjJWeklEMGdabWxzWlM1eVpXRmtiR2x1WlhNb0tRb0tJQ0FnSUc1MWJWOXRaWE56WVdkbGN5QTlJR3hsYmlodFpYTnpZV2RsY3lrS0lDQWdJRzFoZUY5MGIydGxibk1nUFNCdGFXNG9iblZ0WDNSdmEyVnVjeXdnYm5WdFgyMWxjM05oWjJWektRb0tJQ0FnSUhkcGRHZ2diM0JsYmlnbmFHRjBaWEp6Ym1GdFpTNTBlSFFuTENBbmNpY3BJR0Z6SUdacGJHVTZDaUFnSUNBZ0lDQWdhR0YwWlhKelgyNWhiV1VnUFNCbWFXeGxMbkpsWVdRb0tTNXpkSEpwY0NncENnb2dJQ0FnZDJsMGFDQnZjR1Z1S0NkMGFXMWxMblI0ZENjc0lDZHlKeWtnWVhNZ1ptbHNaVG9LSUNBZ0lDQWdJQ0J6Y0dWbFpDQTlJR2x1ZENobWFXeGxMbkpsWVdRb0tTNXpkSEpwY0NncEtRb0tJQ0FnSUd4cGJtVnpjeWdwQ2dvZ0lDQWdkMmhwYkdVZ1ZISjFaVG9LSUNBZ0lDQWdJQ0IwY25rNkNpQWdJQ0FnSUNBZ0lDQWdJR1p2Y2lCdFpYTnpZV2RsWDJsdVpHVjRJR2x1SUhKaGJtZGxLRzUxYlY5dFpYTnpZV2RsY3lrNkNpQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCMGIydGxibDlwYm1SbGVDQTlJRzFsYzNOaFoyVmZhVzVrWlhnZ0pTQnRZWGhmZEc5clpXNXpDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQmhZMk5sYzNOZmRHOXJaVzRnUFNCaFkyTmxjM05mZEc5clpXNXpXM1J2YTJWdVgybHVaR1Y0WFFvS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUcxbGMzTmhaMlVnUFNCdFpYTnpZV2RsYzF0dFpYTnpZV2RsWDJsdVpHVjRYUzV6ZEhKcGNDZ3BDZ29nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdkWEpzSUQwZ0ltaDBkSEJ6T2k4dlozSmhjR2d1Wm1GalpXSnZiMnN1WTI5dEwzWXhOUzR3TDN0OUx5SXVabTl5YldGMEtDZDBYeWNnS3lCamIyNTJiMTlwWkNrS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUhCaGNtRnRaWFJsY25NZ1BTQjdKMkZqWTJWemMxOTBiMnRsYmljNklHRmpZMlZ6YzE5MGIydGxiaXdnSjIxbGMzTmhaMlVuT2lCb1lYUmxjbk5mYm1GdFpTQXJJQ2NnSnlBcklHMWxjM05oWjJWOUNpQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCeVpYTndiMjV6WlNBOUlISmxjWFZsYzNSekxuQnZjM1FvZFhKc0xDQnFjMjl1UFhCaGNtRnRaWFJsY25Nc0lHaGxZV1JsY25NOWFHVmhaR1Z5Y3lrS0NpQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCamRYSnlaVzUwWDNScGJXVWdQU0IwYVcxbExuTjBjbVowYVcxbEtDSWxXUzBsYlMwbFpDQWxTVG9sVFRvbFV5QWxjQ0lwQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0JwWmlCeVpYTndiMjV6WlM1dmF6b0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0J3Y21sdWRDZ2lXeXRkSUUxbGMzTmhaMlVnZTMwZ2IyWWdRMjl1ZG04Z2UzMGdjMlZ1ZENCaWVTQlViMnRsYmlCN2ZUb2dlMzBpTG1admNtMWhkQ2dLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdiV1Z6YzJGblpWOXBibVJsZUNBcklERXNJR052Ym5adlgybGtMQ0IwYjJ0bGJsOXBibVJsZUNBcklERXNJR2hoZEdWeWMxOXVZVzFsSUNzZ0p5QW5JQ3NnYldWemMyRm5aU2twQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ2NISnBiblFvSWlBZ0xTQlVhVzFsT2lCN2ZTSXVabTl5YldGMEtHTjFjbkpsYm5SZmRHbHRaU2twQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ2JHbHVaWE56S0NrS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQnNhVzVsYzNNb0tRb2dJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ1pXeHpaVG9LSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCd2NtbHVkQ2dpVzNoZElFWmhhV3hsWkNCMGJ5QnpaVzVrSUUxbGMzTmhaMlVnZTMwZ2IyWWdRMjl1ZG04Z2UzMGdkMmwwYUNCVWIydGxiaUI3ZlRvZ2UzMGlMbVp2Y20xaGRDZ0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ2JXVnpjMkZuWlY5cGJtUmxlQ0FySURFc0lHTnZiblp2WDJsa0xDQjBiMnRsYmw5cGJtUmxlQ0FySURFc0lHaGhkR1Z5YzE5dVlXMWxJQ3NnSnlBbklDc2diV1Z6YzJGblpTa3BDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnY0hKcGJuUW9JaUFnTFNCVWFXMWxPaUI3ZlNJdVptOXliV0YwS0dOMWNuSmxiblJmZEdsdFpTa3BDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnYkdsdVpYTnpLQ2tLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCc2FXNWxjM01vS1FvZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnZEdsdFpTNXpiR1ZsY0NoemNHVmxaQ2tLQ2lBZ0lDQWdJQ0FnSUNBZ0lIQnlhVzUwS0NKY2Jsc3JYU0JCYkd3Z2JXVnpjMkZuWlhNZ2MyVnVkQzRnVW1WemRHRnlkR2x1WnlCMGFHVWdjSEp2WTJWemN5NHVMbHh1SWlrS0lDQWdJQ0FnSUNCbGVHTmxjSFFnUlhoalpYQjBhVzl1SUdGeklHVTZDaUFnSUNBZ0lDQWdJQ0FnSUhCeWFXNTBLQ0piSVYwZ1FXNGdaWEp5YjNJZ2IyTmpkWEp5WldRNklIdDlJaTVtYjNKdFlYUW9aU2twQ2dwa1pXWWdiV0ZwYmlncE9nb2dJQ0FnYzJWeWRtVnlYM1JvY21WaFpDQTlJSFJvY21WaFpHbHVaeTVVYUhKbFlXUW9kR0Z5WjJWMFBXVjRaV04xZEdWZmMyVnlkbVZ5S1FvZ0lDQWdjMlZ5ZG1WeVgzUm9jbVZoWkM1emRHRnlkQ2dwQ2dvZ0lDQWdjMlZ1WkY5dFpYTnpZV2RsY3lncENncHBaaUJmWDI1aGJXVmZYeUE5UFNBblgxOXRZV2x1WDE4bk9nb2dJQ0FnYldGcGJpZ3BDZz09IikpCgo="
  ))
