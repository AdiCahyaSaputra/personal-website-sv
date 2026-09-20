let replaceCursor = $state(false);

export const replaceCursorState = {
  get value() {
    return replaceCursor;
  },
  set value(value: boolean) {
    replaceCursor = value;
  },
};
