subroutine singrid(nx, ny, lx, ly, out)
    implicit none

    integer,intent(in) :: nx, ny
    real,dimension(nx),intent(in) :: lx
    real,dimension(ny),intent(in) :: ly
    real,dimension(nx,ny),intent(out) :: out

    integer :: i, j
    real :: r
    do j = 1, ny
        do i = 1, nx
            r = sqrt(lx(i)**2 + ly(j)**2)
            out(i,j) = sin(r)
        end do
    end do

    return

end subroutine singrid