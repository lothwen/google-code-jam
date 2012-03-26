;; Common Lisp implementation of http://code.google.com/codejam/contest/351101/dashboard#s=p1

(defun split-by-one-space (string)
    "Returns a list of substrings of string
divided by ONE space each.
Note: Two consecutive spaces will be seen as
if there were an empty string between them."
    (loop for i = 0 then (1+ j)
          as j = (position #\Space string :start i)
          collect (subseq string i j)
          while j))


(let ((n (read-line *terminal-io* nil :eof)))
  (loop for i from 1 to (parse-integer n) do
        (let ((l (read-line *terminal-io* nil :eof)))
          (format t "Case #~S: ~{~A~^ ~}~%" i
                  (nreverse
                   (split-by-one-space l))))))


;; abeaumont's implementation
;(require 'asdf)
;(asdf:oos 'asdf:load-op :split-sequence)

;(loop
;   for i from 1 to (parse-integer (read-line *standard-input*))
;   for s = (split-sequence:split-sequence #\Space (read-line *standard-input*))
;   do (format t "Case #~A:~{ ~A~}~%" i s))
